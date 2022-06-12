from fastapi import APIRouter, Depends
from database import get_db
import schemas
from controllers import book
from sqlalchemy.orm import Session


router = APIRouter(
    tags=['Book']
)

@router.post('/book')
def create(request: schemas.BookCreate, db: Session = Depends(get_db)):
    return book.create(request, db)

@router.get('/book')
def get_all(db: Session = Depends(get_db)):
    return book.get_all(db)

@router.get('/book/{id}')
def get_by_id(id: int, db: Session = Depends(get_db)):
    return book.get_by_id(id, db)

@router.put('/book/{id}')
def update(id: int, request: schemas.BookCreate, db: Session = Depends(get_db)):
    return book.update(id, request, db)

@router.delete('/book/{id}')
def destroy(id: int, db: Session = Depends(get_db)):
    return book.destroy(id, db)