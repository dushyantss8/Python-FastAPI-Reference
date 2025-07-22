# FastAPI CRUD Example

This is a simple FastAPI application that demonstrates basic **CRUD operations for blog posts** using in-memory storage (a Python list). It does not use any views or templates — purely an API backend.

## 📁 Project Structure

```
.
├── main.py         # The main FastAPI application
├── README.md       # Project documentation
└── .gitignore      # Ignored files and folders
```

## 🚀 Features

- 🟢 Get all posts
- 🟡 Create a new post
- 🔵 Get a single post by ID
- 🔴 Delete a post by ID

## 🔧 Requirements

- Python 3.7+
- FastAPI
- Uvicorn

Install dependencies:

```bash
pip install fastapi uvicorn
```

## ▶️ Running the Application

Use `uvicorn` to run the FastAPI app:

```bash
uvicorn main:app --reload
```

- `--reload`: enables hot-reload on code changes (useful for development)

## 🌐 API Endpoints

| Method | Endpoint        | Description                |
|--------|------------------|----------------------------|
| GET    | `/`              | Root message               |
| GET    | `/posts`         | Retrieve all posts         |
| POST   | `/posts`         | Create a new post          |
| GET    | `/posts/{id}`    | Retrieve a post by ID      |
| DELETE | `/posts/{id}`    | Delete a post by ID        |

### Example POST Body

```json
{
  "title": "Sample Title",
  "content": "Sample content goes here",
  "published": true,
  "rating": 5
}
```

## 📦 Notes

- The application uses in-memory storage (`my_posts` list), so data resets every time the server restarts.
- ID is randomly generated using Python's `randrange`.

## 📚 Learn More

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)

---

Happy coding! 🐍