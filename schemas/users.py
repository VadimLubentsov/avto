from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    id: int
    login: EmailStr
    password: str= Field(qe= 5, le=72)

    class Config:
        from_attributes = True


class UserSchemaAdd(BaseModel):
    login: EmailStr
    password: str=Field(qe= 5, le=72)
