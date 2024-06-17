from utils.repository import SQLAlchemyRepostitory
from auth.models import User


class UserRepository(SQLAlchemyRepostitory):
    model = User