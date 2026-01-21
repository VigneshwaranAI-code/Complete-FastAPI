# Book Store API

A RESTful API built with FastAPI for managing a book store. This project uses SQLite as the database and SQLAlchemy for ORM (Object-Relational Mapping).

## Project Structure

The project directory is organized as follows:

```
Connect_to_SQLlite/
├── Database.py      # Database connection and session setup
├── Models.py        # SQLAlchemy database models definition
├── main.py          # Main application entry point and API routes
├── deps.py          # Dependencies (e.g., get_db session)
├── books.db         # SQLite database file (created automatically on first run)
└── README.md        # Project documentation
```

## Tech Stack

*   **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
*   **SQLAlchemy**: The Python SQL toolkit and Object Relational Mapper.
*   **SQLite**: A C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.
*   **Uvicorn**: A lightning-fast ASGI server implementation, using uvloop and httptools.
*   **Pydantic**: Data validation using Python type hints.

## Prerequisites

*   **Python 3.8** or higher

## Installation

1.  **Clone the repository** (if applicable) or navigate to the project directory:
    ```bash
    cd c:/FastAI/Connect_to_SQLlite
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    
    # Activate on Windows
    .\venv\Scripts\activate
    
    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install fastapi uvicorn sqlalchemy
    ```

## Running the Application

Start the development server using Uvicorn:

```bash
uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`.

## API Documentation

FastAPI automatically generates interactive API documentation.

*   **Swagger UI**: Navigate to `http://127.0.0.1:8000/docs` to see the interactive API docs. You can test endpoints directly from the browser.
*   **ReDoc**: Navigate to `http://127.0.0.1:8000/redoc` for an alternative documentation view.

### API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/books` | Retrieve a list of all books |
| `POST` | `/books` | Create a new book |
| `PUT` | `/update/{id}` | Update a book by its ID |
| `DELETE` | `/delete/{id}` | Delete a book by its ID |

#### Example: Create a Book
**POST** `/books`
```json
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "description": "A novel about the American dream",
  "rating": 5
}
```
