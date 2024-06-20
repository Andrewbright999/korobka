from infrastructure.utils.repository import SQLAlchemyRepostitory
from domain.users.models import User


class UserRepository(SQLAlchemyRepostitory):
    model = User