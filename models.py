from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String, null
from database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    pwd = Column(String)
    name = Column(String)
    userable_type = Column(String)
    userable_id = Column(Integer)

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)
    nisn = Column(String)
    denda = Column(Float)

class Librarian(Base):
    __tablename__ = "librarian"

    id = Column(Integer, primary_key=True, index=True)
    nip = Column(String)

class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    isbn = Column(String)
    title = Column(String)
    description = Column(String)
    author = Column(String)
    status_peminjaman = Column(Boolean, default=False)
    tanggal_peminjaman = Column(Date, default=null, nullable=True)

class Log(Base):
    __tablename__ = "log"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user_id = Column(Integer)
    book_title = Column(String)
    tanggal_peminjaman = Column(Date, default=null)
    tanggal_dikembalikan = Column(Date, default=null, nullable=True)