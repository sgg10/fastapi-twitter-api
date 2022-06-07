from typing import Optional
from enum import Enum

# Pydantic
from pydantic import Field
from pydantic import EmailStr
from pydantic import BaseModel

class HairColor(Enum):
    WHITE: str = "white"
    BROWN: str = "brown"
    BLACK: str = "black"
    BLOND: str = "blond"
    RED:   str = "red"

class PersonBase(BaseModel):
    first_name: str = Field(
        ...,
        min_length=0,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=0,
        max_length=50
    )
    age: int = Field(
        ...,
        ge=18,
        le=100
    )
    email: EmailStr = Field(
        ...,
        title = "Email",
        description = "The email of the person"
    )
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)

class Person(PersonBase):
    password: str = Field(..., min_length=8, max_length=50)

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Sebastian",
                "last_name": "Granda Gallego",
                "age": 21,
                "email": "sebastiangg10@hotmail.com",
                "hair_color": "black",
                "is_married": False,
                "password": "sebastian123456789"
            }
        }

class PersonOut(PersonBase):
    pass