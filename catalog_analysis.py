import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movie_list):
    """Return the catalog's average rating rounded to one decimal place."""
    total_rating = sum(movie["rating"] for movie in movie_list)
    return round(total_rating / len(movie_list), 1)


def catalog_age_stats(movie_list, current_year=2026):
    """Return the oldest, newest, and rounded-up average movie age."""
    ages = [current_year - movie["year"] for movie in movie_list]
    average_age = math.ceil(sum(ages) / len(ages))
    return max(ages), min(ages), average_age


def duration_in_hours(minutes):
    """Convert a duration in minutes to a human-readable hours/minutes string."""
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}ч {remaining_minutes}м"


def rating_tier(rating):
    """Categorize a numeric movie rating."""
    if rating >= 9:
        return "шедевр"
    if rating >= 7:
        return "хорошо"
    return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    """Categorize a release year using guarded structural pattern matching."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


def print_non_comedy_titles(movie_list):
    """Print every movie title except comedies using continue."""
    for movie in movie_list:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(movie_list):
    """Find and return the first movie rated above 9 using while/break/else."""
    index = 0
    while index < len(movie_list):
        movie = movie_list[index]
        if movie["rating"] > 9.0:
            break
        index += 1
    else:
        print("Шедевров не найдено")
        return None
    return movie


def count_long_movies(movie_list, threshold=120):
    """Count movies whose duration is greater than the threshold."""
    count = 0
    for movie in movie_list:
        if movie["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title):
    """Normalize every word's first letter without using str.title()."""
    normalized_words = []
    for word in title.split():
        normalized_words.append(word[0].upper() + word[1:])
    return " ".join(normalized_words)


def make_slug(title):
    """Convert a normalized movie title to a lowercase hyphenated slug."""
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    """Format one movie as a line in the catalog report."""
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}"
    )


def titles_sorted_by_rating(movie_list):
    """Return titles ordered from highest rating to lowest."""
    sorted_movies = sorted(
        movie_list,
        key=lambda movie: movie["rating"],
        reverse=True,
    )
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movie_list, n=3):
    """Return the top n movies as title/rating tuples."""
    sorted_movies = sorted(
        movie_list,
        key=lambda movie: movie["rating"],
        reverse=True,
    )
    return [
        (movie["title"], movie["rating"])
        for movie in sorted_movies[:n]
    ]


def count_by_genre(movie_list):
    """Count movies for each genre using dict.get()."""
    genre_counts = {}
    for movie in movie_list:
        for genre in movie["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts


def actor_filmography(movie_list):
    """Build a mapping from every actor to their movie titles."""
    filmography = {}
    for movie in movie_list:
        for actor in movie["actors"]:
            filmography.setdefault(actor, []).append(movie["title"])
    return filmography


def ratings_above_average(movie_list):
    """Return a title/rating dictionary for above-average movies."""
    catalog_average = average_rating(movie_list)
    return {
        movie["title"]: movie["rating"]
        for movie in movie_list
        if movie["rating"] > catalog_average
    }


def all_genres(movie_list):
    """Return the union of all genre sets in the catalog."""
    genres = set()
    for movie in movie_list:
        genres.update(movie["genres"])
    return genres


def common_actors(movie1, movie2):
    """Return actors shared by two movies using set intersection."""
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    """Return genres present in movies_a but absent from movies_b."""
    return all_genres(movies_a) - all_genres(movies_b)


def iter_high_rated(movie_list, min_rating=8.0):
    """Yield movies whose rating is at least min_rating."""
    for movie in movie_list:
        if movie["rating"] >= min_rating:
            yield movie


def print_high_rated_movies(movie_list, min_rating=8.0):
    """Demonstrate consuming iter_high_rated with a for loop."""
    for movie in iter_high_rated(movie_list, min_rating):
        print(format_report_line(movie))


def total_duration_above_rating(movie_list, min_rating=7):
    """Sum durations lazily for movies rated above min_rating."""
    return sum(
        movie["duration_min"]
        for movie in movie_list
        if movie["rating"] > min_rating
    )


def build_report(movie_list):
    """Print the complete catalog report."""
    _, _, average_age = catalog_age_stats(movie_list)
    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movie_list)}")
    print(f"Средний возраст фильмов: {average_age} лет")

    print("\nТоп-3 фильма:")
    top_movies = sorted(
        movie_list,
        key=lambda movie: movie["rating"],
        reverse=True,
    )[:3]
    for movie in top_movies:
        print(f"  {format_report_line(movie)}")

    print("\nФильмов по жанрам:")
    genre_counts = count_by_genre(movie_list)
    sorted_genres = sorted(
        genre_counts,
        key=lambda genre: (-genre_counts[genre], genre),
    )
    for genre in sorted_genres:
        print(f"  {genre} — {genre_counts[genre]}")

    genres = ", ".join(sorted(all_genres(movie_list)))
    print(f"\nВсе жанры каталога: {genres}")


if __name__ == "__main__":
    build_report(movies)
