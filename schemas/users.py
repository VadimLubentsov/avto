from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    id: int
    login: EmailStr
    password: str= Field()

    class Config:
        from_attributes = True


class UserSchemaAdd(BaseModel):
    login: EmailStr
    password: str=Field(min_length=5, max_length=72)
