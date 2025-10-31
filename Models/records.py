import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base
from schemas.records import  RecordSchema


class Records(Base):
    __tablename__ = "records"

    id: Mapped[int] = mapped_column(primary_key = True)
    mark: Mapped[str]
    model: Mapped[str]
    value_engine: Mapped[float]
    color: Mapped[str]
    user_id: Mapped[int]= mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    created_ad: Mapped[datetime.datetime] = mapped_column(server_default=func.now())

    def to_read_model(self) -> RecordSchema:
        return RecordSchema(
            id=self.id,
            mark=self.mark,
            model=self.model,
            value_engine=self.value_engine,
            color=self.color,
            user_id=self.user_id,
            created_ad=self.created_ad
        )