from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from database import AsyncSession, get_async_session
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy

from auth.models import User


JWT_SECRET = "SECRET"

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=JWT_SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

