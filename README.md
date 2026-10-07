# Bookstore REST API

A full-fledged, production-ready REST API for managing bookstore inventory. This project is built using modern Python backend technologies, focusing on clean architecture, modularity, and maintainability.

🚀 Tech Stack

  **Framework:** [FastAPI](https://fastapi.tiangolo.com/) - High performance, easy to learn, fast to code, ready for production.
  **Database:** SQLite - Lightweight, file-based database perfect for local development.
  **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/) - The Python SQL toolkit and Object Relational Mapper.
   **Validation:** [Pydantic v2](https://docs.pydantic.dev/) - Data validation and settings management using Python type annotations.
   **Server:** [Uvicorn](https://www.uvicorn.org/) - An ASGI web server implementation for Python.

## ✨ Features

   **CRUD Operations:** Fully functional endpoints to Create, Read, Update, and Delete books.
   **Advanced Filtering:** Search for books by partial title match, author name, or price range (`min_price`, `max_price`).
   **Data Validation:** Strict payload validation ensures required fields, proper data types, and logical constraints (e.g., price > 0).
   **Error Handling:** Robust HTTP exception handling for scenarios like duplicate ISBNs (409) or unfound records (404).
   **Interactive Documentation:** Auto-generated Swagger UI and ReDoc interfaces available out-of-the-box.

## 📁 Project Structure

```text
bookstore_api/
├── app/
│   ├── __init__.py
│   ├── main.py               # Application entry point & configuration
│   ├── database.py           # SQLAlchemy setup and session dependency
│   ├── models.py             # SQLAlchemy Database ORM Models
│   ├── schemas.py            # Pydantic schemas for request/response validation
│   └── routers/
│       ├── __init__.py
│       └── books.py          # API route definitions for /books
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## 🛠️ Installation & Setup

Follow these steps to run the project locally on your machine.

### 1. Clone or Create the Project Directory
Ensure all files from the project structure above are saved in a folder named `bookstore_api`. Open your terminal and navigate into this folder.

### 2. Create a Virtual Environment
It is best practice to use a virtual environment to manage your dependencies.
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
*   **Windows (PowerShell):**
    ```powershell
    .\venv\Scripts\activate
    ```
*   **macOS / Linux:**
    ```bash
    source venv/bin/activate
    ```

### 4. Install Dependencies
Install all required packages from the `requirements.txt` file.
```bash
pip install -r requirements.txt
```

## 🏃‍♂️ Running the Server

Start the Uvicorn development server. The `--reload` flag enables auto-reloading when you make code changes.

```bash
uvicorn app.main:app --reload
```

*Note: The SQLite database (`bookstore.db`) will be created automatically in your root directory the first time the server starts.*

## 📖 API Documentation

Once the server is running, you can interact with the API using the automatic, interactive documentation provided by FastAPI:

*   **Swagger UI:** Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.
*   **ReDoc:** Navigate to [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

## 🧪 Testing with Postman

You can easily test the API using Postman:
1. Copy the raw JSON collection provided during the setup phase.
2. Save it as `bookstore-api.postman_collection.json`.
3. Open Postman and click **Import**.
4. Drag and drop the file to load the collection.
5. Ensure your local server is running and start testing the endpoints!

---
*Built with ❤️ using FastAPI and Python.*