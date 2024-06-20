from fastapi_users import BaseUserManager, InvalidID
from fastapi_users.exceptions import UserAlreadyExists

from domain.users.models import User, Role
from infrastructure.utils.config import settings


class UserManager(BaseUserManager[User, int]):
    def parse_id(self, value: int) -> int:
        try:
            return int(value)
        except ValueError as e:
            raise InvalidID() from e 
        
    reset_password_token_secret = settings.SECRET_AUTH
    verification_token_secret = settings.SECRET_AUTH

    async def on_after_register(self, user: User, request = None):
        user.is_active = True
        user.is_verified = True
        user.is_superuser = False
        print(f"User {user.id} has registered.")

        
    




