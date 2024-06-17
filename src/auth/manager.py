from typing import Optional

from fastapi_users import FastAPIUsers
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, InvalidID

from auth.models import User
from auth.auth_backend import get_user_db, auth_backend


AUTH_SECRET = "SECRET"


class UserManager(BaseUserManager[User, int]):
    def parse_id(self, value: int) -> int:
        try:
            return int(value)
        except ValueError as e:
            raise InvalidID() from e 
    reset_password_token_secret = AUTH_SECRET
    verification_token_secret = AUTH_SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        user.is_active = True
        user.is_verified = True
        user.is_superuser = False
        print(f"User {user.id} has registered.")
        

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
    
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()

