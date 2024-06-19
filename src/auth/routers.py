from typing import Annotated, List

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from auth.auth_backend import auth_backend
from auth.schemas import UserRead, UserCreate, PassUserRead
from auth.models import User
from auth.manager import fastapi_users, current_user
from services.users import UserService
from dependecies import admin_role_check, user_service, admin_role_check


router = APIRouter(tags=["User"])


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
)


router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    dependencies=[Depends(admin_role_check)],
    prefix="/auth",
)


@router.get("/users")
async def get_all_users(
    user_service: Annotated[UserService, Depends(user_service)],
    user: User = Depends(admin_role_check),
) -> List[PassUserRead]: 
    """Получить список всех пользователей"""
    users = await user_service.find_all_users()
    if len(users) == 0:
        raise JSONResponse(status_code=404, content={"details":"Пользователей нет"})
    return users


@router.get("/users/profile")
async def get_user_profile(
    user_service: Annotated[UserService, Depends(user_service)],
    user: User = Depends(current_user),
)-> PassUserRead:
    """Получить профиль пользователя"""
    user = await user_service.find_one(user_id=user.id)
    return user

