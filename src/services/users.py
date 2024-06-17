from utils.repository import AbstractRepository
# from schemas import AddBoxRequest, AddBox, Status

class UserService:
    def __init__(self, box_repo: AbstractRepository):
        self.box_repo: AbstractRepository = box_repo()
        
    # async def add_box(self, box: AddBoxRequest, user_id: int):
    #     box_dict = AddBox(**box.model_dump(), user_id=user_id).model_dump()
    #     print(box_dict)
    #     box_id = await self.box_repo.add_one(box_dict)
    #     return box_id
    
    async def find_all_users(self):
        boxes = await self.box_repo.find_all()
        return boxes
    
    async def find_one(self, user_id:int):
        boxes = await self.box_repo.find_all(id = user_id)
        return boxes
    
