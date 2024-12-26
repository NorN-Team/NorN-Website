from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from models.movie_structure import MovieDB, Genre, movie_genre_association  # Импортируем модели SQLAlchemy

def filter_movies(
    db: Session,
    title_substr: Optional[str] = None,
    genres: Optional[List[str]] = None,
    year_range: Optional[tuple] = None
) -> List[MovieDB]:
    """
    Фильтрует фильмы в базе данных по переданным параметрам.

    :param db: Сессия базы данных.
    :param title_substr: Подстрока, которая должна быть в названии (необязательно).
    :param genres: Список жанров, которые должны быть у фильма (необязательно).
    :param year_range: Диапазон лет (кортеж из двух чисел), например (1990, 2000) (необязательно).
    :return: Отфильтрованный список фильмов.
    """
    # Начинаем с базового запроса
    query = db.query(MovieDB)

    # Фильтрация по подстроке в названии
    if title_substr:
        query = query.filter(MovieDB.title.ilike(f"%{title_substr}%"))
        print(f"Фильтрация по названию ({title_substr}): выполнен запрос")

    # Фильтрация по жанрам
    if genres:
        query = query.join(movie_genre_association).join(Genre).filter(Genre.name.in_(genres))
        print(f"Фильтрация по жанрам ({genres}): выполнен запрос")

    # Фильтрация по диапазону лет
    if year_range:
        start_year, end_year = year_range
        query = query.filter(MovieDB.year.between(start_year, end_year))
        print(f"Фильтрация по диапазону лет ({start_year}-{end_year}): выполнен запрос")

    # Выполняем запрос и возвращаем результат
    return query.all()

# Пример использования
if __name__ == "__main__":
    from services.filter import get_db  # Импортируем функцию для получения сессии базы данных

    # Получаем сессию базы данных
    db = next(get_db())

    # Тестирование фильтрации
    filtered_movies = filter_movies(db, title_substr="Matrix", genres=["Action"], year_range=(1990, 2000))
    for movie in filtered_movies:
        print(movie.title, movie.year)