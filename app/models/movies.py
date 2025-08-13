from uuid import uuid4

from pydantic import BaseModel, Field


class Movie(BaseModel):
    id: str = Field(default_factory=lambda: uuid4().hex)
    title: str
    description: str
    release_year: int
