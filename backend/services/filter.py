from typing import List, Optional, Tuple
from models.movie_structure import Movie

def filter(
    movies: List[Movie],
    title_substr: Optional[str] = None,
    genres: Optional[List[str]] = None,
    year_range: Optional[Tuple[int, int]] = None,
) -> List[Movie]:
    """
    Фильтрует список фильмов по названию, жанрам и диапазону годов.

    :param movies: Список фильмов для фильтрации.
    :param title_substr: Подстрока, которая должна быть в названии фильма.
    :param genres: Список жанров для фильтрации.
    :param year_range: Кортеж с начальным и конечным годом.
    :return: Отфильтрованный список фильмов.
    """
    filtered = movies

    # Фильтрация по названию
    if title_substr:
        filtered = [
            movie for movie in filtered if title_substr.lower() in movie.title.lower()
        ]

    # Фильтрация по жанрам
    if genres:
        filtered = [
            movie for movie in filtered if any(genre in movie.genres for genre in genres)
        ]

    # Фильтрация по диапазону лет
    if year_range:
        start_year, end_year = year_range
        filtered = [
            movie for movie in filtered if start_year <= movie.year <= end_year
        ]

    return filtered
