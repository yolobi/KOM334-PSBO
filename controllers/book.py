from datetime import datetime
from fastapi import Depends, HTTPException, status
from sqlalchemy import null
from sqlalchemy.orm import Session
from database import get_db
import schemas, models

def create(request: schemas.BookCreate, db: Session = Depends(get_db)):
    new_book = models.Book(isbn=request.isbn, title=request.title, description=request.description, author=request.author, status_peminjaman=False, tanggal_peminjaman=datetime.now())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def get_all(db: Session = Depends(get_db)):
    books = db.query(models.Book).all()
    return books

def get_by_id(id:int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} is not found")
    return book

def update(id: int, request: schemas.BookCreate, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} is not found")

    book.update(request.dict())
    db.commit()
    return book.first()

def destroy(id:int , db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == id)
    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} is not found")
    book.delete(synchronize_session=False)
    db.commit()
    return 'Deleted'