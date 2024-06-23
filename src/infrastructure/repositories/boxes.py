from infrastructure.utils.repository import SQLAlchemyRepostitory
from domain.boxes.models import Box

class BoxRepository(SQLAlchemyRepostitory):
    model = Box