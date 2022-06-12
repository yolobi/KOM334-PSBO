from fastapi import Depends

from database import get_db
import schemas, models
from sqlalchemy.orm import Session

def create_from_student(request: schemas.UserBase, id:int, db: Session = Depends(get_db)):
    new_user = models.User(email=request.email, password=request.password, name=request.name, userable_type="Student", userable_id=id)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user