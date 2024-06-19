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
    except:
        return JSONResponse(status_code=404, content={"detail":"Box not found"})