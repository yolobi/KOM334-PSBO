from fastapi import FastAPI
from pydantic import BaseModel

class Account(BaseModel):
    no_borrowed_books : str
    no_reserved_books : str
    no_returned_books : str
    no_lost_books : str
    fine_amount : float
    
