from typing import Optional
from fastapi import APIRouter, Depends

from database import get_db
from sqlalchemy.orm import Session
from controllers import student
from oauth2 import get_current_user
import schemas


router = APIRouter(
    prefix='/student',
    tags=['Student']
)

@router.get('/search')
def search_book(query: Optional[str], db: Session = Depends(get_db)):
    return student.search_book(query, db)

@router.post('/')
def create(request: schemas.StudentCreate, db: Session = Depends(get_db)):
    return student.create(request, db)

@router.get('/')
def get_all(db: Session = Depends(get_db)):
    return student.get_all(db)

@router.get('/{id}')
def get_by_id(id: int, db: Session = Depends(get_db)):
    return student.get_by_id(id, db)

@router.put('/{id}')
def update(id: int, request: schemas.StudentBase, db: Session = Depends(get_db)):
    return student.update(id, request, db)

@router.delete('/{id}')
def destroy(id: int, db: Session = Depends(get_db)):
    return student.destroy(id, db)

@router.put('/pinjam/{uid}/{bid}')
def pinjam_buku(uid: int, bid:int, db: Session = Depends(get_db)):
    return student.pinjam_buku(uid, bid, db)

@router.put('/kembalikan/{uid}/{bid}')
def kembalikan_buku(uid: int, bid: int, db: Session = Depends(get_db)):
    return student.kembalikan_buku(uid, bid, db)