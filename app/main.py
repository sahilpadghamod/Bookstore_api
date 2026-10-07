from fastapi import FastAPI
from app.database import engine, Base
from app.routers import books

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Bookstore Inventory API",
    description="A production-ready REST API for managing bookstore inventory.",
    version="1.0.0",
)

# Register routers
app.include_router(books.router)

@app.get("/", tags=["Health Check"])
def health_check():
    return {"status": "ok", "message": "Bookstore API is running gracefully."}