from typing import List

from fastapi import Depends, FastAPI, HTTPException
from matplotlib.style import use
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import models, schemas

from routers import book, librarian, log, student, user

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(book.router)
# app.include_router(librarian.router)
# app.include_router(log.router)
app.include_router(student.router)
# app.include_router(user.router)