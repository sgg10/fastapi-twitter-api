from uuid import UUID
from typing import Optional
from datetime import date

from pydantic import BaseModel
from pydantic import SecretStr
from pydantic import EmailStr
from pydantic import Field
from pydantic import ValidationError, validator

class BaseUser(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class User(BaseUser):
    first_name: str = Field(
        ...,
        min_length=3,
        max_length=50
    )
    first_name: str = Field(
        ...,
        min_length=3,
        max_length=50
    )
    birth_date: date = Field(...)
    gender: Optional[str] = Field(default=None)

    @validator('birth_date')
    def is_over_eighteen(cls, v):
        today = date.today()
        delta = today - v
        if delta.days/365 <= 18:
            raise ValueError("Must be over 18!")
        return v

class UserLogin(BaseUser):
    password: SecretStr = Field(
        ...,
        min_length=8,
        max_length=32,
        regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,32}$",
        description="Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one number and one special character."
    )