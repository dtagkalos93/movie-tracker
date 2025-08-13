from pydantic import BaseModel


class MovieIn(BaseModel):
    title: str
    description: str
    release_year: int
