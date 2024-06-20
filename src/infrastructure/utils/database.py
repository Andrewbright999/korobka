from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

from infrastructure.utils.config import settings


class Base(DeclarativeBase):    
    def __repr__(self) -> str:
        cols = []
        for col in self.__table__.columns.keys():
            cols.append(f"{col} = {getattr(self, col)}")
        return f"<{self.__class__.__name__} {','.join(cols)}>"
    pass 

metadata = MetaData()

engine = create_async_engine(
    url = settings.DATABASE_URL_asyncpg,
    # echo=True,  
)

async_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_async_session():
    async with async_session() as session:
        yield session

async def create_tables(): 
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        
        
