from utils.repository import AbstractRepository
from boxes.schemas import AddBoxRequest, AddBox, Status

class BoxService:
    def __init__(self, box_repo: AbstractRepository):
        self.box_repo: AbstractRepository = box_repo()
        
    async def add_box(self, box: AddBoxRequest, user_id: int):
        box_dict = AddBox(**box.model_dump(), user_id=user_id).model_dump()
        print(box_dict)
        box_id = await self.box_repo.add_one(box_dict)
        return box_id
    
    async def find_courier_boxes(self, user_id: int):
        boxes = await self.box_repo.find_all(user_id = user_id)
        return boxes
    
    async def find_actual_courier_boxes(self, user_id: int):
        boxes = await self.box_repo.find_all_in_status(status = [Status.DELIVERY, Status.NEW],user_id = user_id,)
        return boxes
    
    async def update_box_status(self,box_id: int, user_id: int, status: Status):
        box_id = await self.box_repo.update_box(box_id=box_id, user_id = user_id, status = status)
        return box_id
    
    async def find_boxes_id(self, id: int):
        boxes = await self.box_repo.find_all(id = id)
        return boxes