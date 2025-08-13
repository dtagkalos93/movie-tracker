from app.models.movies import Movie
from app.repositories.movies_repository import MoviesRepository
from app.schemas.movies import MovieIn


class MoviesService:
    def __init__(self, movies_repository: MoviesRepository):
        self._movies_repository = movies_repository

    def save(self, movie_in: MovieIn):
        movie = self._convertToModel(movie_in)
        self._movies_repository.save(movie)

    @staticmethod
    def _convertToModel(movie_in: MovieIn) -> Movie:
        return Movie(
            title=movie_in.title,
            description=movie_in.description,
            release_year=movie_in.release_year,
        )
