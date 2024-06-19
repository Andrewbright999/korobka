from typing import Annotated, List

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from auth.manager import current_user
from auth.models import User
from boxes.schemas import UpdateStatus, OnCreateBox, AddBoxRequest, BoxSchema, BoxRead

from services.boxes import BoxService
from dependecies import box_service, courier_role_check,storage_role_check


router = APIRouter(prefix="/api",tags=["Boxes"], )
    
@router.post('/boxes')
async def add_box(
    box: AddBoxRequest, 
    box_service: Annotated[BoxService, Depends(box_service)],
    user: User = Depends(storage_role_check),
    ) -> OnCreateBox:
    """Создание новой коробки"""
    box_id = await box_service.add_box(box, user_id=user.id)
    return JSONResponse(status_code=201, content={"box_id": box_id})


@router.get("/boxes/my")
async def get_my_boxes(
    box_service: Annotated[BoxService, Depends(box_service)],
    user: User = Depends(courier_role_check),
) -> List[BoxSchema]:
    """Все коробки для курьера"""
    try:
        boxes = await box_service.find_courier_boxes(user_id=user.id)
        return boxes
    except:
        return JSONResponse(status_code=500, content={"detail":"Что-то сломалось"})
    

@router.get("/boxes")
async def get_all_boxes(
    box_service: Annotated[BoxService, Depends(box_service)],
    user: User = Depends(storage_role_check),
) -> List[BoxRead]:
    """Все коробки для склада"""
    try:
        boxes = await box_service.find_storage_boxes()
        if len(boxes) == 0:
            return JSONResponse(status_code=404, content={"details":"Коробок нет"})
        return boxes
    except:
        return JSONResponse(status_code=500, content={"detail":"Что-то сломалось"})



@router.get("/boxes/{id}")
async def find_box(
    id:int,
    box_service: Annotated[BoxService, Depends(box_service)],
    user: User = Depends(current_user),
) -> BoxSchema:
    """Получение данных о конкретной коробке"""
    try:
        box = await box_service.find_boxes_id(id=id)
        return box
    except IndexError:
        return JSONResponse(status_code=404, content={"detail": "Коробка не найдена"})


@router.put('/boxes/{id}')
async def update_box_status(
    id:int,
    status: UpdateStatus,
    box_service: Annotated[BoxService, Depends(box_service)],
    user: User = Depends(courier_role_check),
) -> OnCreateBox:
    """Обновление статуса коробки"""
    try:
        box_id = await box_service.update_box_status(box_id=id ,user_id=user.id, status=status)
        return JSONResponse(status_code=201, content={"box_id": box_id})
    except:
        return JSONResponse(status_code=404, content={"detail":"Box not found"})