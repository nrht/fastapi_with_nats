from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import TIMESTAMP


class UserBase(BaseModel):
    email: str
    name: str

class UserCreate(UserBase):
    password: str
    role_id: int
    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    registered_at: datetime
    role_id: int
    class Config:
        orm_mode = True

class RoleBase(BaseModel):
    role: str

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id: int
    users: List[User] = []
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None