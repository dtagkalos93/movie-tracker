from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, HTTPException

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
    start: int = 0, limit: int = 25, service: MoviesService = MOVIE_DEPENDENCY
) -> list[MovieOut]:
    return service.retrieve(start=start, limit=limit)


@router.get("/movies/{movie_id}", response_model=MovieOut)
def retrieve_move(
    movie_id: UUID, service: MoviesService = MOVIE_DEPENDENCY
) -> MovieOut:
    movie = service.retrieve_by_id(movie_id)
    if movie is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Movie not found")
    return service.retrieve_by_id(movie_id)


@router.delete("/movies/{movie_id}", status_code=HTTPStatus.NO_CONTENT)
def delete(movie_id: UUID, service: MoviesService = MOVIE_DEPENDENCY):
    deleted = service.delete(movie_id)
    if not deleted:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Movie not found")
    return {"message": "Movie deleted"}
