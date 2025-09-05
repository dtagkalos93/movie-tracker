from uuid import UUID

from app.models.movies import Movie
from app.repositories.movies_repository import MoviesRepository
from app.schemas.movies import MovieIn, MovieOut


class MoviesService:
    def __init__(self, movies_repository: MoviesRepository):
        self._movies_repository = movies_repository

    def save(self, movie_in: MovieIn):
        movie = Movie(**movie_in.model_dump())
        self._movies_repository.save(movie)

    def retrieve(self, start: int, limit: int) -> list[MovieOut]:
        movies = self._movies_repository.retrieve(start=start, limit=limit)
        movies_out: list[MovieOut] = list()
        for movie in movies:
            movies_out.append(MovieOut(**movie.model_dump()))
        return movies_out

    def retrieve_by_id(self, movie_id: UUID) -> MovieOut | None:
        movie = self._movies_repository.retrieve_by_id(movie_id)
        print(movie)
        if movie is None:
            return None

        return MovieOut(**movie.model_dump())

    def delete(self, movie_id: UUID) -> bool:
        return self._movies_repository.delete(movie_id)
