from pydantic import BaseModel
from typing import List, Optional

class AlertBase(BaseModel):
    coin_symbol: str
    target_price: float

class AlertCreate(AlertBase):
    pass

class Alert(AlertBase):
    id: int
    status: str
    owner_id: int

    class Config:
        orm_mode = True

class AlertList(BaseModel):
    alerts: List[Alert]
    total: int

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
