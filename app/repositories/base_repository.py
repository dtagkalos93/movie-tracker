from app.models.movies import Movie


class BaseRepository:
    movies: list[Movie]
