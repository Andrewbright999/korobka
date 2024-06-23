from enum import StrEnum
from fastapi_users import schemas
from pydantic import BaseModel


class Role(StrEnum):
    Admin = "Администратор"
    Storage = "Склад"
    Courier = "Курьер"
    

class UserRead(schemas.BaseUser[int]):
    id: int
    phone: str
    email: str
    first_name: str
    second_name: str
    role: Role


class UserCreate(schemas.BaseUserCreate):
    email: str
    phone: str
    first_name: str
    second_name: str
    role: Role


class ClearUserRead(BaseModel):
    id: int
    email: str
    phone: str
    first_name: str
    second_name: str
    role: Role
    
    
class PassUserRead(ClearUserRead):
    hashed_password: str