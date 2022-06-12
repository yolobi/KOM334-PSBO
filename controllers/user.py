from fastapi import Depends, HTTPException, status

from database import get_db
import schemas, models
from sqlalchemy.orm import Session


def get_all(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

def get_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not found")
    return user

def update(id: int, request: schemas.UserBase, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not found")
    user.update(request)
    return user.first()

def destroy(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not found")
    user.delete(synchronize_session=False)
    return 'Deleted'