from datetime import datetime
from pydantic import BaseModel
from enum import StrEnum



class Size(StrEnum):
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"


class UpdateStatus(StrEnum):
    DELIVERY = "Доставка"
    DONE = "Завершен"


class Status(StrEnum):
    NEW = "Новый"
    DELIVERY = "Доставка"
    DONE = "Завершен"
    
    
class AddBoxRequest(BaseModel):
    size: Size
    address: str
    phone: str
    client: str
    class Config:   
        from_attributes = True


class AddBox(AddBoxRequest):
    user_id: int
    status: Status = Status.NEW


class BoxSchema(AddBoxRequest):
    id: int
    size: Size
    address: str
    phone: str
    client: str
    user_id: int
    status: Status