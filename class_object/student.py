from fastapi import FastAPI
from pydantic import BaseModel
from class_object import User

class Student(User):
    Class : str
    