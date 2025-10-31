from Models.users import UsersOrm
from utils.repository import SQLAlchemyRepository


class UsersRepositories(SQLAlchemyRepository):
    model = UsersOrm