from fastapi import FastAPI
from pydantic import BaseModel

class libraryDatabase(BaseModel):
    list_of_books : str