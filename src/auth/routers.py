from typing import Annotated

from fastapi import APIRouter, Depends

from auth.auth_backend import auth_backend
from auth.schemas import UserRead, UserCreate
from auth.models import User
from auth.manager import fastapi_users
from dependecies import admin_role_check
from services.users import UserService
from dependecies import user_service, admin_role_check



router = APIRouter(prefix="")


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    dependencies=[Depends(admin_role_check)],
    prefix="/auth",
    tags=["auth"],
)


@router.get("/users",tags=["User"])
async def find_login_courier_box(
    user_service: Annotated[UserService, Depends(user_service)],
    user: User = Depends(admin_role_check),
):
    """Получить всех пользователей"""
    # try: 
    users = await user_service.find_all_users()
    return users

