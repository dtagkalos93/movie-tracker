from app.models.movies import Movie
from app.repositories.base_repository import BaseRepository


class MoviesRepository(BaseRepository):
    def save(self, movie: Movie):
        movie_length = len(self.movies)
        movie.id = movie_length
        self.movies.append(movie)
