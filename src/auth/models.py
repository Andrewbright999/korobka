from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from fastapi_users.db import SQLAlchemyBaseUserTable

from database import Base
from auth.schemas import PassUserRead, Role

class User(SQLAlchemyBaseUserTable, Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    boxes = relationship("Box", back_populates="user")
    role = Column(Enum(Role), default=Role.Courier)
    
    def to_read_model(self) -> PassUserRead:
        return PassUserRead(
            id = self.id,
            first_name = self.first_name,
            second_name = self.second_name,
            email = self.email,
            phone = self.phone,
            role = self.role,
            hashed_password = self.hashed_password,
        )