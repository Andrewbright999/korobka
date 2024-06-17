from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response, JSONResponse
from sqlalchemy.exc import NoResultFound

from boxes.schemas import AddBoxRequest
from auth.manager import current_user
from boxes.schemas import UpdateStatus
from auth.schemas import Role
from boxes.models import Box
from auth.models import User
from services.boxes import BoxService
from dependecies import box_service, courier_role_check,storage_role_check


router = APIRouter(prefix="/api",tags=["Boxes"])

# @router.post('/box')
# async def add_box(box_id:int = Depends(create_box)):
#     """Добавление новой коробки"""
#     return {
#     "status":"201",
#     "box_id": box_id
#         }
    
@router.post('/boxes')
async def add_box(
    box: AddBoxRequest, 
    box_service: Annotated[BoxService, Depends(box_service)],
    user: User = Depends(storage_role_check),
    ):
    """Добавление новой коробки"""
    box_id = await box_service.add_box(box, user_id=user.id)
    return JSONResponse(status_code=201, content={"box_id": box_id})


@router.get("/boxes/my")
async def find_login_courier_box(
    box_service: Annotated[BoxService, Depends(box_service)],
    user: User = Depends(courier_role_check),
):
    """Все коробки авторизованного курьера"""
    # try: 
    boxes = await box_service.find_courier_boxes(user_id=user.id)
    return boxes



# @router.get("/box/my/actual")
# async def find_actual_login_courier_box(
#     box_service: Annotated[BoxService, Depends(box_service)],
#     user: User = Depends(current_user),
# ):
#     """Все коробки авторизованного курьера"""
    
#     boxes = await box_service.find_actual_courier_boxes(user_id=user.id)
#     return boxes

@router.get("/boxes")
async def find_boxes(
    box_service: Annotated[BoxService, Depends(box_service)],
    user: User = Depends(storage_role_check),
):
    """Все коробки склада"""
    boxes = await box_service.find_storage_boxes()
    return boxes

@router.get("/boxes/{id}")
async def find_box_id(
    id:int,
    box_service: Annotated[BoxService, Depends(box_service)],
    user: User = Depends(current_user),
):
    """Получение данных о конкретной коробке"""
    boxes = await box_service.find_boxes_id(id=id)
    return boxes


@router.put('/boxes/{id}')
async def update_box_status(
    id:int,
    status: UpdateStatus,
    box_service: Annotated[BoxService, Depends(box_service)],
    user: User = Depends(courier_role_check),
):
    """Обновление статуса коробки"""
    try:
        box_id = await box_service.update_box_status(box_id=id ,user_id=user.id, status=status)
        return JSONResponse(status_code=201, content={"box_id": box_id})
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Box not found")

    
# @router.get('/box')
# async def get_all(session: AsyncSession = Depends(get_async_session)):
#     "Получение всех коробок"
#     query = select(Box, User.first_name, User.second_name).join(User)
#     boxes = await session.execute(query)
#     # выводим результат
#     result = [{'id': box.id, 'size': box.size, 'status': box.status, 'address': box.address, 'phone': box.phone, 'client': box.client, 'User': f"{first_name} {last_name[:1]}"} for box, first_name, last_name in boxes.all()]
#     return result


# @router.get("/first")
# async def get_all(session: AsyncSession = Depends(get_async_session)):
#     query = (
#         select(User)
#         .options(selectinload(User.boxes))
#         )
#     print(query)
#     res = await session.execute(query)
#     res = res.unique().scalars().all()
#     print(res)
#     return res

# @router.get("/box/my")
# async def get_all(session: AsyncSession = Depends(get_async_session),user: User = Depends(current_user)):
#     query = select(Box).filter_by(user_id=user.id)
#     res = await session.execute(query)
#     res_orm = res.scalars().all()
#     # result_validate = [UserBoxRead.model_validate(row, from_attributes=True) for row in res_orm]
#     return res_orm

# @router.get("/user")
# def protected_route(user: User = Depends(current_user)):
#     return f"Hello, {user.id}"