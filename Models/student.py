from fastapi import FastAPI
from pydantic import BaseModel

class Student(BaseModel):
    Class : str
    