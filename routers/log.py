from fastapi import APIRouter, Depends

from database import get_db
from sqlalchemy.orm import Session
from controllers import log
from oauth2 import get_current_user
import schemas


router = APIRouter(
    prefix='/log',
    tags=['Log']
)

@router.post('/')
def create(request: schemas.LogBase, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(get_current_user)):
    return log.create(request, db)

@router.get('/')
def get_all(db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(get_current_user)):
    return log.get_all(db)

@router.get('/{id}')
def get_by_id(id: int, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(get_current_user)):
    return log.get_by_id(id, db)

@router.put('/{id}')
def update(id: int, request: schemas.LogBase, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(get_current_user)):
    return log.update(id, request, db)

@router.delete('/{id}')
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(get_current_user)):
    return log.destroy(id, db)