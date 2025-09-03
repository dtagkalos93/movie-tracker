from pydantic import BaseModel


class BaseMovie(BaseModel):
    title: str
    description: str
    release_year: int


class MovieIn(BaseMovie):
    """Movie in schema"""


class MovieOut(BaseMovie):
    id: str
