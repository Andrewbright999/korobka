from abc import abstractmethod, ABC
from sqlalchemy import insert, select, update
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import NoResultFound
from sqlalchemy import desc
from auth.models import User



from database import async_session

class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError
    
    @abstractmethod
    async def find_all():
        raise NotImplementedError
    
    @abstractmethod
    async def find_all_in_status():
        raise NotImplementedError
    
    @abstractmethod
    async def update_box():
        raise NotImplementedError
    
    @abstractmethod
    async def get_storage_boxes():
        raise NotImplementedError
    
    @abstractmethod
    async def get_courier_boxes():
        raise NotImplementedError
    
    @abstractmethod
    async def get_all_couriers():
        raise NotImplementedError
    
    @abstractmethod
    async def get_all_couriers():
        raise NotImplementedError
    
    
class SQLAlchemyRepostitory(AbstractRepository):
    model = None
    
    async def add_one(self, data: dict):
        async with async_session() as session:
            stmt = insert(self.model).values(data).returning(self.model.id)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar_one()
    
    async def find_all(self, **params):
        async with async_session() as session:
            querty = select(self.model).filter_by(**params).order_by(desc(self.model.id))
            result = await session.execute(querty)
            result = [row[0].to_read_model() for row in result.all()]
            return result

    async def find_all_in_status(self, status: list, **params):
        async with async_session() as session:
            querty = select(self.model).filter_by(**params).filter(self.model.status.in_(status))
            result = await session.execute(querty)
            result = [row[0].to_read_model() for row in result.all()]
            return result
        
    async def update_box(self, box_id, **params) -> int:
        async with async_session() as session:
            stmt = update(self.model).where(self.model.id == box_id).values(**params).returning(self.model.id)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar_one()
        
    async def get_storage_boxes(self):
        async with async_session() as session:
            querty = (select(self.model)
                      .options(joinedload(self.model.user))
                      )
            result = await session.execute(querty)  
            result = [{
            "id": box.id,
            "size": box.size,
            "address": box.address,
            "phone": box.phone,
            "client": box.client,
            "courier": f"{box.user.first_name} {box.user.second_name[:1]}",
            "status": box.status
            } for box in result.scalars().all()]
            return result
    
    
    async def get_courier_boxes():
        raise NotImplementedError
    
    async def get_all_couriers():
        raise NotImplementedError
    
    async def get_all_couriers():
        raise NotImplementedError