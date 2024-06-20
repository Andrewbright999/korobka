from fastapi import Depends, HTTPException
from infrastructure.utils.auth import current_user
from domain.users.schemas import Role
from domain.users.models import User
from infrastructure.repositories.boxes import BoxRepository
from infrastructure.repositories.users import UserRepository
from application.services.boxes import BoxService
from application.services.users import UserService



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