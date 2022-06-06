# Pydantic
from pydantic import Field
from pydantic import EmailStr
from pydantic import BaseModel


class LoginOut(BaseModel):
    username: str = Field(..., max_length=20, example="sgg10")
    message: str = Field(example="Login Succesfuly!")