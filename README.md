# Bookstore Enterprise REST API

A full-fledged, production-ready REST API for managing bookstore inventory. This project is built using modern Python backend technologies and features enterprise-grade upgrades including containerization, robust relational databases, stateless authentication, and caching.

## 🚀 Tech Stack

*   **Framework:** [FastAPI](https://fastapi.tiangolo.com/) - High performance, easy to learn, fast to code, ready for production.
*   **Database:** [PostgreSQL](https://www.postgresql.org/) - Advanced, enterprise-level open-source relational database.
*   **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/) - The Python SQL toolkit and Object Relational Mapper.
*   **Caching:** [Redis](https://redis.io/) - In-memory data structure store used to drastically reduce API latency.
*   **Authentication:** JWT (JSON Web Tokens) with Passlib and Bcrypt for secure password hashing and stateless session management.
*   **Infrastructure:** [Docker & Docker Compose](https://www.docker.com/) - Containerization for seamless, environment-agnostic deployment.

## ✨ Features

*   **Containerized Deployment:** Spin up the application, PostgreSQL, and Redis simultaneously using a single Docker Compose command.
*   **Secure Authentication:** OAuth2 password bearer flow with JWT secures the `POST`, `PUT`, and `DELETE` endpoints. 
*   **High-Performance Caching:** Redis automatically caches the results of inventory searches, significantly reducing database load on repeated queries.
*   **CRUD Operations:** Fully functional endpoints to Create, Read, Update, and Delete books.
*   **Advanced Filtering:** Search for books by partial title match, author name, or price range.
*   **Data Validation:** Strict payload validation using Pydantic v2 ensures proper data types and logical constraints.

## 📁 Project Structure

```text
bookstore_api/
├── app/
│   ├── __init__.py
│   ├── main.py               # Application entry point & configuration
│   ├── database.py           # PostgreSQL connection & SQLAlchemy setup
│   ├── models.py             # User and Book ORM Models
│   ├── schemas.py            # Pydantic schemas for request/response validation
│   ├── auth.py               # JWT encoding/decoding and password hashing
│   └── routers/
│       ├── __init__.py
│       ├── auth.py           # Login and registration routes
│       └── books.py          # Protected API route definitions for /books
├── docker-compose.yml        # Multi-container orchestration 
├── Dockerfile                # Image instructions for the FastAPI app
└── requirements.txt          # Python dependencies
