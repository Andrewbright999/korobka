from utils.repository import SQLAlchemyRepostitory
from boxes.models import Box

class BoxRepository(SQLAlchemyRepostitory):
    model = Box