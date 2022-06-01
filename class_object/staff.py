from fastapi import FastAPI
from pydantic import BaseModel
from class_object.user import User

class Staff(User):
    dept : str
    