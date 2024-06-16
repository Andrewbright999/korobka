from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from boxes.schemas import BoxSchema, Size, Status

class Box(Base):
    __tablename__ = "box"
    
    id = Column(Integer, primary_key=True, index=True)
    size = Column(Enum(Size))
    status = Column(Enum(Status), default=Status.NEW)
    address = Column(String)
    phone = Column(String)
    client = Column(String)
    user_id = Column(
        Integer, ForeignKey("user.id"), unique=False, nullable=False
    )
    user = relationship("User", back_populates="boxes")
    
    def to_read_model(self) -> BoxSchema:
        return BoxSchema(
            id=self.id,
            size = self.size,
            address = self.address,
            phone = self.phone,
            client = self.client,
            user_id = self.user_id,
            status = self.status,
        )



