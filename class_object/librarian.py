from fastapi import FastAPI
from pydantic import BaseModel

class Librarian(BaseModel):
    name : str
    id : str
    password : str
    searchString : str
    
