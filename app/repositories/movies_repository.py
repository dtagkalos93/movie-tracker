from uuid import UUID

from app.models.movies import Movie


class MoviesRepository:
    movies: list[Movie] = []  # class-level attribute, shared across all instances

    def save(self, movie: Movie):
        MoviesRepository.movies.append(movie)

    def retrieve(self, start: int, limit: int) -> list[Movie]:
        return MoviesRepository.movies[start:limit]

    def retrieve_by_id(self, movie_id: UUID) -> Movie | None:
        for movie in MoviesRepository.movies:
            if movie.id == movie_id.hex:
                return movie
        return None

    def delete(self, movie_id) -> bool:
        for idx, movie in enumerate(MoviesRepository.movies):
            if movie.id == movie_id.hex:
                del MoviesRepository.movies[idx]
                return True
        return False
