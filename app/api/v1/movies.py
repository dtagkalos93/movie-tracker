from fastapi import APIRouter

from app.dependencies import MOVIE_DEPENDENCY
from app.schemas.movies import MovieIn, MovieOut
from app.services.movies_service import MoviesService

router = APIRouter(tags=["Movie"])


@router.post("/movies", response_model=MovieIn)
def store_movie(payload: MovieIn, service: MoviesService = MOVIE_DEPENDENCY) -> MovieIn:
    service.save(payload)
    return payload


@router.get("/movies", response_model=list[MovieOut])
def retrieve_movies(
    page: int = 0, limit: int = 25, service: MoviesService = MOVIE_DEPENDENCY
) -> list[MovieOut]:
    return list()
