from fastapi import Depends, HTTPException

from auth.manager import current_user
from auth.schemas import Role
from auth.models import User
from repositories.boxes import BoxRepository
from repositories.users import UserRepository
from services.boxes import BoxService
from services.users import UserService


def box_service():
    return BoxService(BoxRepository)

def user_service():
    return UserService(UserRepository)

def admin_role_check(user: User = Depends(current_user)):
    if user.role != Role.Admin:
        raise HTTPException(
            status_code=403,
            detail="Вы не администратор"
        )
    else:
        return user
        
def courier_role_check(user: User = Depends(current_user)):
    if user.role not in [Role.Admin, Role.Courier]:
        raise HTTPException(
            status_code=403,
            detail="Вы не курьер"
        )
    else:
        return user

def storage_role_check(user: User = Depends(current_user)):
    if user.role not in [Role.Admin, Role.Storage]:
        raise HTTPException(
            status_code=403,
            detail="Вы не сотрудник склада"
        )
    else:
        return user