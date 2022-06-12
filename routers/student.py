from fastapi import APIRouter, Depends

from database import get_db
from sqlalchemy.orm import Session
from controllers import student
import schemas


router = APIRouter(
    tags=['Student']
)

@router.post('/student')
def create(request: schemas.StudentCreate, db: Session = Depends(get_db)):
    return student.create(request, db)