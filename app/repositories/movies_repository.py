from uuid import UUID

from app.models.movies import Movie


class MoviesRepository:
    movies: list[Movie] = []  # class-level attribute, shared across all instances

    def save(self, movie: Movie):
        MoviesRepository.movies.append(movie)
        print(MoviesRepository.movies)

    def retrieve(self, start: int, limit: int) -> list[Movie]:
        print(MoviesRepository.movies)
        return MoviesRepository.movies[start:limit]

    def retrieve_by_id(self, movie_id: UUID) -> Movie | None:
        print(movie_id)
        for movie in MoviesRepository.movies:
            print(movie)
            if movie.id == movie_id.hex:
                return movie
        return None
