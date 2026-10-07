from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import date, datetime

class BookBase(BaseModel):
    title: str = Field(..., min_length=1, description="Title of the book")
    author: str = Field(..., min_length=1, description="Author of the book")
    isbn: str = Field(..., min_length=10, max_length=17, description="Unique ISBN code")
    price: float = Field(..., gt=0, description="Price must be greater than 0")
    stock_quantity: int = Field(0, ge=0, description="Stock cannot be negative")
    published_date: Optional[date] = Field(None, description="Date of publication")

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    author: Optional[str] = Field(None, min_length=1)
    isbn: Optional[str] = Field(None, min_length=10, max_length=17)
    price: Optional[float] = Field(None, gt=0)
    stock_quantity: Optional[int] = Field(None, ge=0)
    published_date: Optional[date] = None

class BookResponse(BookBase):
    id: str
    created_at: datetime
    updated_at: datetime

    # Pydantic v2 configuration to allow ORM model serialization mapping
    model_config = ConfigDict(from_attributes=True)