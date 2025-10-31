from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    login: str
    password: str

    class Config:
        from_attributes = True


class UserSchemaAdd(BaseModel):
    login: str
    password: str
