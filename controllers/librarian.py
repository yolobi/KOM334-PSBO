from typing import Optional
from fastapi import Depends, HTTPException, status
from database import get_db
import schemas, models
from sqlalchemy.orm import Session
from controllers import book

def create(request: schemas.LibrarianBase, db: Session = Depends(get_db)):
    new_librarian = models.Librarian(nip=request.nip)
    db.add(new_librarian)
    db.commit()
    db.refresh(new_librarian)
    new_user = models.User(email=request.email, pwd=request.password, name=request.name, userable_type="Librarian", userable_id=new_librarian.id)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all(db: Session = Depends(get_db)):
    librarians = db.query(models.Librarian).all()
    return librarians

def get_by_id(id: int, db: Session = Depends(get_db)):
    librarian = db.query(models.Librarian).filter(models.Librarian.id == id).first()
    if not librarian:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Librarian with id {id} is not found")
    return librarian

def update(id: int, request: schemas.LibrarianBase, db: Session = Depends(get_db)):
    librarian = db.query(models.Librarian).filter(models.Librarian.id == id)
    if not librarian:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Librarian with id {id} is not found")
    librarian.update(request)
    db.commit()
    return librarian

def destroy(id: int, db: Session = Depends(get_db)):
    librarian = db.query(models.Librarian).filter(models.Librarian.id == id)
    if not librarian.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Librarian with id {id} is not found")
    librarian.delete(synchronize_session=False)
    db.commit()
    return 'Deleted'

def add_book(request: schemas.BookCreate, db: Session = Depends(get_db)):
    return book.create(request, db)

def destroy_book(id: int, db: Session = Depends(get_db)):
    return book.destroy(id, db)

def edit_book(id: int, request: schemas.BookCreate, db: Session = Depends(get_db)):
    return book.update(id, request, db)

def search_book(query: Optional[str], db: Session = Depends(get_db)):
    res = db.query(models.Book).filter(models.Book.title.contains(query)).all()
    return res

def inspect(id: int, db: Session = Depends(get_db)):
    books = db.query(models.Book).filter(models.Book.id_peminjam == id).all()
    return books