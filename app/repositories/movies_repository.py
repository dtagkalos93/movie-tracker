from app.models.movies import Movie


class MoviesRepository:
    movies: list[Movie] = []  # class-level attribute, shared across all instances

    def save(self, movie: Movie):
        MoviesRepository.movies.append(movie)
        print(self.movies)
