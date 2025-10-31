from sqlalchemy.orm import Mapped, mapped_column
from db.db import Base
from schemas.users import UserSchema


class UsersOrm(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key = True)
    login: Mapped[str]
    password: Mapped[str]

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            login=self.login,
            password=self.password
        )