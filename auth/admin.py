import contextlib

from fastapi_users.exceptions import UserAlreadyExists

from database import get_async_session
from auth.auth_backend import get_user_db
from auth.schemas import UserCreate, Role
from auth.manager import get_user_manager
from config import settings


get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)

async def create_admin():
    email= settings.ROOT_EMAIL
    password = settings.ROOT_PASSWORD
    phone = settings.ROOT_PHONE
    first_name= settings.FIRST_NAME
    second_name = settings.SECOND_NAME
    is_superuser = settings.SUPER_USER
    role = Role.Admin
    try:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    user = await user_manager.create(
                        UserCreate(
                            email=email, password=password, phone = phone, is_superuser=is_superuser,first_name = first_name, second_name=second_name, role = role
                        )
                    )
                    print(f"User created {user}")
                    return user
    except UserAlreadyExists:
        pass