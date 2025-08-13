from fastapi import APIRouter

from app.dependencies import MOVIE_DEPENDENCY
from app.schemas.movies import MovieIn
from app.services.movies_service import MoviesService

router = APIRouter()


@router.post("/movies", response_model=MovieIn, tags=["Movie"])
def store_movie(payload: MovieIn, service: MoviesService = MOVIE_DEPENDENCY) -> MovieIn:
    service.save(payload)
    return payload
