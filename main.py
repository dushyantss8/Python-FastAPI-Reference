from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException 
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [
    {
        "id": 1,
        "title": "Post 1 title",
        "content": "Post 1 content",
    },
    {
        "id": 2,
        "title": "Post 2 title",
        "content": "Post 2 content",
    }
]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        
def find_post_index(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

# This is called a path operation function, it is a function that is called when a request is made to the path /
# The @app.get decorator is used to define a path operation function that will be called when a GET request is made to the path /
# It is the same as other frameworks call it a route handler
@app.get("/")
def read_root():
    return {"message": "I love python."}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.model_dump()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {
        "message": "Post created successfull!",
        "post": post_dict
    }

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)   # Need to convert to an integer because cant compare int to str
    if not post:
        # This one is better.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found.")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return { "message": "Post not found." }
    return {
        "message": "Post content",
        "post": post
    }

# APIs with the same pattern should not be created like this
# The following route matched previous signature so can never be reached here
# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[len(my_posts)-1]
#     return {"latest_post": post}

# @app.post("/create-post")
# # def create_post(payload: dict = Body(...)):
# def create_post(new_post: Post):
#     print("new_post Payload: ", new_post)
#     print("Converted to dict using model_dump: ", new_post.model_dump())
#     return {
#         "message": "Post created successfully!",
#         "data": new_post.model_dump()
#         # "title": new_post.title,
#         # "content": new_post.content,
#         # "published": new_post.published,
#         # "rating": new_post.rating,
#     }

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # deleting post
    # find the index in the array that has required ID
    index = find_post_index(id)
    
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found.")
    
    my_posts.pop(index)
    # return { "message": "Post deleted successfully!" }  # Id deleting then dont return json like this
    return Response(status_code=status.HTTP_204_NO_CONTENT) # Instead return a response like this