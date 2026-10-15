from fastapi import FastAPI
from app.database import engine, Base
from app.routers import books, auth

# Auto-generate PostgreSQL tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bookstore Enterprise API")

app.include_router(auth.router)
app.include_router(books.router)