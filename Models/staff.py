from fastapi import FastAPI
from pydantic import BaseModel

class Staff(BaseModel):
    dept : str
    