import os
import json
import redis
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.models import Book, User
from app.schemas import BookCreate, BookUpdate, BookResponse
from app.auth import get_current_user

router = APIRouter(prefix="/books", tags=["Books"])

# Initialize Redis client
redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
redis_client = redis.Redis.from_url(redis_url, decode_responses=True)

def clear_book_cache():
    """Flushes cached GET requests when modifications happen"""
    for key in redis_client.scan_iter("books_cache:*"):
        redis_client.delete(key)

@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if db.query(Book).filter(Book.isbn == book.isbn).first():
        raise HTTPException(status_code=409, detail="ISBN already exists.")
    
    new_book = Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    clear_book_cache()
    return new_book

@router.get("/", response_model=List[BookResponse])
def get_books(
    author: Optional[str] = Query(None),
    title: Optional[str] = Query(None),
    min_price: Optional[float] = Query(None),
    max_price: Optional[float] = Query(None),
    db: Session = Depends(get_db)
):
    # 1. Check Redis Cache
    cache_key = f"books_cache:{author}:{title}:{min_price}:{max_price}"
    cached_data = redis_client.get(cache_key)
    
    if cached_data:
        return json.loads(cached_data)

    # 2. Query Database if cache miss
    query = db.query(Book)
    if author: query = query.filter(Book.author.ilike(f"%{author}%"))
    if title: query = query.filter(Book.title.ilike(f"%{title}%"))
    if min_price is not None: query = query.filter(Book.price >= min_price)
    if max_price is not None: query = query.filter(Book.price <= max_price)
    
    results = query.all()
    
    # 3. Serialize and Store in Cache for 1 hour
    serialized_results = [BookResponse.model_validate(b).model_dump(mode="json") for b in results]
    redis_client.setex(cache_key, 3600, json.dumps(serialized_results))
    
    return results

@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: str, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book: raise HTTPException(status_code=404, detail="Book not found.")
    return book

@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: str, update_data: BookUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book: raise HTTPException(status_code=404, detail="Book not found.")
    
    update_dict = update_data.model_dump(exclude_unset=True)
    for key, value in update_dict.items():
        setattr(book, key, value)
        
    db.commit()
    db.refresh(book)
    clear_book_cache()
    return book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book: raise HTTPException(status_code=404, detail="Book not found.")
    
    db.delete(book)
    db.commit()
    clear_book_cache()
    return None