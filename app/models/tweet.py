from uuid import UUID
from typing import Optional
from datetime import date, datetime

from pydantic import BaseModel
from pydantic import Field

from .user import User

class Tweet(BaseModel):
    tweet_id: UUID
    content: str = Field(
        ...,
        min_length=1,
        max_length=280
    )
    created_at: date = Field(default=datetime.now())
    updated_at: Optional[date] = Field(default=None)
    by: User = Field(...)
