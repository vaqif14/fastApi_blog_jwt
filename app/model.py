from pydantic import BaseModel, Field, EmailStr


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example":   {
                      "title": "IT INNOVATIONS",
                      "content": "The IT Innovations course is the best course in the world"
    }
        }


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Vaqif Gulmammadov",
                "email": "vaqif@itinnovations.az",
                "password": "Inno12345"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "vaqif@itinnovations.az",
                "password": "Inno12345"
            }
        }
