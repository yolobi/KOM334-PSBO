from datetime import datetime
from typing import List, Optional
from unicodedata import name
from pydantic import BaseModel
from pyrsistent import s
from sqlalchemy import Date

class BookBase(BaseModel):
    isbn: str
    title: str
    description: str
    author: str
    status_peminjaman: bool
    tanggal_peminjaman: datetime

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True

class StudentBase(UserBase):
    nisn: str
    books: List[BookBase]
    denda: float

    class Config:
        orm_mode = True

class LibrarianBase(UserBase):
    nip: str

    class Config:
        orm_mode = True

class LogBase(BaseModel):
    name: str
    book_title: str
    user_id: int
    tanggal_peminjaman: datetime
    tanggal_dikembalikan: datetime

    class Config:
        orm_mode = True

class LogCreate(BaseModel):
    name: str
    book_title: str
    user_id: int

class StudentCreate(UserBase):
    nisn: str

class BookCreate(BaseModel):
    isbn: str
    title: str
    description: str
    author: str

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None