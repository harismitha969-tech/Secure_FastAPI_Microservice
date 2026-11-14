
from pydantic import BaseModel, EmailStr
from typing import Optional


# User Registration Schema
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# User Response Schema
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True


# User Login Schema
class UserLogin(BaseModel):
    username: str
    password: str


# Item Creation Schema
class ItemCreate(BaseModel):
    title: str
    description: Optional[str] = None


# Item Response Schema
class ItemResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    owner_id: int

    class Config:
        from_attributes = True
