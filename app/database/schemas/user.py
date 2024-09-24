from typing import List, Union
from pydantic import BaseModel
from .item import Item

class UserBase(BaseModel):
    email: str

class UserCreate(BaseModel):
    email: str
    password: str


class User(BaseModel):
    id: int
    email: str
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
