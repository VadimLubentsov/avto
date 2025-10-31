from abc import ABC, abstractmethod
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import async_session_maker
class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError

class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session


    async def add_one(self, data: dict) -> int:
         stmt = insert(self.model).values(**data).returning(self.model.id)
         res = await self.session.execute(stmt)
         return res.scalar_one()

    async def find_all(self) -> list:
            stmt = select(self.model)
            res = await self.session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res

    async def login_exists(self, login: str) -> bool:
        stmt = select(self.model).where(self.model.login == login)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()
        return user is not None
