from fastapi import Depends, HTTPException, status
from database import get_db
import schemas, models
from sqlalchemy.orm import Session
from hashing import Hash
from .import log


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