import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Float, Integer, Date, DateTime
from app.database import Base

def get_utc_now():
    return datetime.now(timezone.utc)

class Book(Base):
    __tablename__ = "books"

    # Using UUIDs over auto-incrementing integers for production-grade security
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, index=True, nullable=False)
    author = Column(String, index=True, nullable=False)
    isbn = Column(String, unique=True, index=True, nullable=False)
    
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, default=0, nullable=False)
    published_date = Column(Date, nullable=True)
    
    # Audit timestamps
    created_at = Column(DateTime, default=get_utc_now, nullable=False)
    updated_at = Column(DateTime, default=get_utc_now, onupdate=get_utc_now, nullable=False)