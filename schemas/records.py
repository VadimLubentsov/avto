
from typing import Optional

from pydantic import BaseModel


class RecordSchema(BaseModel):

    id: int
    mark: str
    model:str
    value_engine:float
    color: str
    user_id: int


    class Config:
        from_attributes = True


class RecordSchemaAdd(BaseModel):
    mark: str
    model: str
    value_engine: float
    color: str
    user_id: int
