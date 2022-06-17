from datetime import datetime, date
from typing import Optional
from fastapi import Depends, HTTPException, status
from database import get_db
import schemas, models
from sqlalchemy.orm import Session
from hashing import Hash


def create(request: schemas.StudentCreate, db: Session = Depends(get_db)):
    new_student = models.Student(nisn=request.nisn, denda=0)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    db_student = db.query(models.Student).filter(models.Student.nisn == request.nisn).first()
    
    hashedPassword = Hash.bcrypt(request.password)
    new_user = models.User(email=request.email, pwd=hashedPassword, name=request.name, userable_type="Student", userable_id=db_student.id)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all(db: Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return students

def get_by_id(id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with id {id} is not found")
    return student

def update(id: int, request: schemas.StudentBase, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with id {id} is not found")
    student.update(request)
    db.commit()
    return student.first()

def destroy(id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with id {id} is not found")
    student.delete(synchronize_session=False)
    db.commit()
    return 'Deleted'

def pinjam_buku(uid: int, bid: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == bid)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {bid} is not found")
    book.update({'id_peminjam' : uid, 'status_peminjaman' : True, 'tanggal_peminjaman' : datetime.now()})
    db.commit()
    return f"buku {book.first().title} telah dipinjam"

def kembalikan_buku(uid: int, bid: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == uid)
    book = db. query(models.Book).filter(models.Book.id == bid)
    if not book or not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    tax = book.first().tanggal_peminjaman
    tax = (date.today() - tax)
    book.update({'status_peminjaman': False, 'tanggal_peminjaman': date.today(), 'id_peminjam': 0})
    student.update({'denda': tax.days})
    db.commit()
    return f"buku {book.first().title} telah berhasil dikembalikan"

def search_book(query: Optional[str], db: Session = Depends(get_db)):
    books = db.query(models.Book).filter(models.Book.title.contains(query), models.Book.status_peminjaman == False)
    return books.all()