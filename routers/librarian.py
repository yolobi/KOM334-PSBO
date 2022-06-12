from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from controllers import librarian
from oauth2 import get_current_user
import schemas

router = APIRouter(
    prefix='/librarian',
    tags=['Librarian']
)

@router.get('/search')
def search(query: Optional[str], db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(get_current_user)):
    return librarian.search_book(query, db)

@router.post('/')
def create(request: schemas.LibrarianBase, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(get_current_user)):
    return librarian.create(request, db)

@router.get('/')
def get_all(db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(get_current_user)):
    return librarian.get_all(db)

@router.get('/{id}')
def get_by_id(id: int, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(get_current_user)):
    return librarian.get_by_id(id, db)

@router.put('/{id}')
def update(id: int, request: schemas.LibrarianBase, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(get_current_user)):
    return librarian.update(id, request, db)

@router.delete('/{id}')
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(get_current_user)):
    return librarian.destroy(id, db)

@router.post('/add_book')
def add_book(request: schemas.BookCreate, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(get_current_user)):
    return librarian.add_book(request, db)

@router.delete('/delete_book/{id}')
def destroy_book(id: int, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(get_current_user)):
    return librarian.destroy_book(id, db)

@router.put('/update_book/{id}')
def edit_book(id: int, request: schemas.BookCreate, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(get_current_user)):
    return librarian.edit_book(id, request, db)