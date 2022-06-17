from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from controllers import user
from oauth2 import get_current_user
import schemas


router = APIRouter(
    prefix='/user',
    tags=['User']
)
@router.get('/')
def get_all(db: Session = Depends(get_db)):
    return user.get_all(db)

@router.get('/{id}')
def get_by_id(id: int, db: Session = Depends(get_db)):
    return user.get_by_id(id, db)

@router.put('/{id}')
def update(id: int, request: schemas.UserBase, db: Session = Depends(get_db)):
    return user.update(id, request, db)

@router.delete('/{id}')
def destroy(id: int, db: Session = Depends(get_db)):
    return user.destroy(id, db)