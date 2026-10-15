from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import date, datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class UserCreate(BaseModel):
    username: str
    password: str

class BookBase(BaseModel):
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    isbn: str = Field(..., min_length=10, max_length=17)
    price: float = Field(..., gt=0)
    stock_quantity: int = Field(0, ge=0)
    published_date: Optional[date] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    price: Optional[float] = None
    stock_quantity: Optional[int] = None
    published_date: Optional[date] = None

class BookResponse(BookBase):
    id: str
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)