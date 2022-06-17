from fastapi import FastAPI
from database import engine
import models
from routers import book, librarian, log, student, user, auth

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.get('/')
def root():
    return 'TUGAS AKHIR PSBO - KOM334'

app.include_router(auth.router)
app.include_router(book.router)
app.include_router(librarian.router)
app.include_router(log.router)
app.include_router(student.router)
app.include_router(user.router)