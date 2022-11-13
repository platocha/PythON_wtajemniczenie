def print_top_movies(movies, *, number_of_movies = 10):
    movies_in_rate_order = sorted(movies, key=lambda single_movie: single_movie.rate, reverse=True)
    for index, movie in enumerate(movies_in_rate_order):
        if index < number_of_movies:
            print(f"{index+1}. {movie}")