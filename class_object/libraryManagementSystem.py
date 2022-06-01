from fastapi import FastAPI
from pydantic import BaseModel

class LibrayManagementSystem(BaseModel):
    userType : str
    username : str
    password : str 