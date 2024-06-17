from utils.repository import SQLAlchemyRepostitory
from boxes.models import User

class UserRepository(SQLAlchemyRepostitory):
    model = User