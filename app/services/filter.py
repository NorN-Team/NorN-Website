from typing import List, Optional
from models.movie_structure import Movie

def filter_movies(movies: List[Movie], title_substr: Optional[str] = None, genres: Optional[List[str]] = None, year_range: Optional[tuple] = None) -> List[Movie]:
    """
    Фильтрует массив фильмов по переданным параметрам.

    :param movies: Список фильмов для фильтрации.
    :param title_substr: Подстрока, которая должна быть в названии (необязательно).
    :param genres: Список жанров, которые должны быть у фильма (необязательно).
    :param year_range: Диапазон лет (кортеж из двух чисел), например (1990, 2000) (необязательно).
    :return: Отфильтрованный список фильмов.
    """
    # Начинаем с оригинального списка
    filtered = movies

    # Фильтрация по названию
    if title_substr:
        filtered = [movie for movie in filtered if title_substr.lower() in movie.title.lower()]
        print(f"Фильтрация по названию ({title_substr}): найдено {len(filtered)} фильмов")

    # Фильтрация по жанрам
    if genres:
        filtered = [movie for movie in filtered if all(genre in movie.genres for genre in genres)]
        print(f"Фильтрация по жанрам ({genres}): найдено {len(filtered)} фильмов")

    # Фильтрация по диапазону лет
    if year_range:
        start_year, end_year = year_range
        filtered = [movie for movie in filtered if start_year <= movie.year <= end_year]
        print(f"Фильтрация по диапазону лет ({start_year}-{end_year}): найдено {len(filtered)} фильмов")

    return filtered

# Пример использования
if __name__ == "__main__":
    from models.movie_structure import movies

    # Тестирование фильтрации
    print(filter_movies(movies, title_substr="Matrix", genres=["Action"], year_range=(1990, 2000)))
