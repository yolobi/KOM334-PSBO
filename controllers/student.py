from fastapi import Depends

from database import get_db
import schemas, models
from sqlalchemy.orm import Session

def create(request: schemas.StudentCreate, db: Session = Depends(get_db)):
    new_student = models.Student(nisn=request.nisn, denda=0)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    db_student = db.query(models.Student).filter(models.Student.nisn == request.nisn).first()
    new_user = models.User(email=request.email, password=request.password, name=request.name, userable_type="Student", userable_id=db_student.id)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_student