from datetime import datetime
from typing import List
from unicodedata import name
from pydantic import BaseModel
from sqlalchemy import Date

class BookBase(BaseModel):
    isbn: str
    title: str
    description: str
    author: str
    status_peminjaman: bool
    tanggal_peminjaman: datetime

class UserBase(BaseModel):
    name: str
    email: str
    password: str

class StudentBase(UserBase):
    nisn: str
    books: List[BookBase]
    denda: float

class LibrarianBase(UserBase):
    nip: str

class LogBase(BaseModel):
    name: str
    book_title: str
    tanggal_peminjaman: datetime
    tanggal_dikembalikan: datetime

class StudentCreate(UserBase):
    nisn: str

class BookCreate(BaseModel):
    isbn: str
    title: str
    description: str
    author: str