from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class ItemBase(BaseModel):
    name: str
    email: EmailStr
    item_name: str
    quantity: int
    expiry_date: date

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    name: Optional[str]
    item_name: Optional[str]
    quantity: Optional[int]
    expiry_date: Optional[date]

class ItemResponse(ItemBase):
    insert_date: date
