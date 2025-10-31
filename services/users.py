from schemas.users import UserSchemaAdd
from utils.unitofwork import IUnitOfWork
from fastapi import HTTPException
from utils.hash_password import hash_password
class UsersService:
    async def add_user(self, uow: IUnitOfWork, user: UserSchemaAdd) -> int:
        user_dict = user.model_dump()
        async with uow:
            user_id = await uow.users.add_one(user_dict)
            await uow.commit()
            return user_id

    async def get_users(self, uow: IUnitOfWork) -> list:
        async with uow:
            users = await uow.users.find_all()
            return users

    async def register_user(self, uow: IUnitOfWork, user: UserSchemaAdd) -> int:
        async with uow:
            if await uow.users.login_exists(user.login):
                raise HTTPException(
                    status_code=400,
                    detail="Пользователь с таким логином уже существует"
                )
            user_dict = user.model_dump()
            user_dict['password'] = hash_password(user_dict['password'])
            user_id = await uow.users.add_one(user_dict)
            await uow.commit()
            return user_id

