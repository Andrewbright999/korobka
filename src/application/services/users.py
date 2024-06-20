from infrastructure.utils.repository import AbstractRepository

class UserService:
    def __init__(self, user_repo: AbstractRepository):
        self.user_repo: AbstractRepository = user_repo()
        
    async def find_all_users(self):
        users = await self.user_repo.find_all()
        return users
    
    async def find_one(self, user_id:int):
        users = await self.user_repo.find_all(id = user_id)
        return users[0]
    
