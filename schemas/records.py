from pydantic import BaseModel, Field


class RecordSchema(BaseModel):

    id: int
    mark: str=Field(max_length=80)
    model:str=Field(max_length=80)
    value_engine:float = Field(qe=0.8, le= 15)
    color: str=Field(max_length=40)
    user_id: int


    class Config:
        from_attributes = True


class RecordSchemaAdd(BaseModel):
    mark: str
    model: str
    value_engine: float
    color: str
    user_id: int
