from datetime import datetime
from fastapi import Depends, HTTPException, status

from database import get_db
import schemas, models
from sqlalchemy.orm import Session

def create(request: schemas.LogCreate, db: Session = Depends(get_db)):
    new_log = models.Log(name=request.name, book_title=request.book_title, user_id=request.user_id, tanggal_peminjaman=datetime.now(), tanggal_dikembalikan=datetime.now())
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log

def get_all(db: Session = Depends(get_db)):
    logs = db.query(models.Log).all()
    return logs

def get_by_id(id: int, db: Session = Depends(get_db)):
    log = db.query(models.Log).filter(models.Log.id == id).first()
    if not log:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"log with id {id} is not found")
    return log

def update(id: int, request: schemas.LogBase, db: Session = Depends(get_db)):
    log = db.query(models.Log).filter(models.Log.id == id)
    if not log:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"log with id {id} is not found")
    log.update(request)
    db.commit()
    return log.first()

def destroy(id: int, db: Session = Depends(get_db)):
    log = db.query(models.Log).filter(models.Log.id == id)
    if not log:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"log with id {id} is not found")
    log.delete(synchronize_session=False)
    db.commit()
    return 'Deleted'