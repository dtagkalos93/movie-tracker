from pydantic import BaseModel


class Movie(BaseModel):
    id: int
    title: str
    description: str
    release_year: int
