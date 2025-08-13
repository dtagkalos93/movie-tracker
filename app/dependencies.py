from fastapi import Depends

from app.repositories.movies_repository import MoviesRepository
from app.services.movies_service import MoviesService


def get_movie_service():
    return MoviesService(movies_repository=MoviesRepository())


MOVIE_DEPENDENCY = Depends(get_movie_service)
