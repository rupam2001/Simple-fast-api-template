from typing import Union
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None

class ItemCreate(BaseModel):
    pass

class Item(BaseModel):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
