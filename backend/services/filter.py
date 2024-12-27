from typing import List, Optional, Tuple
from settings import get_connection


def get_genre_ids_by_names(genre_names: List[str]) -> List[int]:
    """
    Получает идентификаторы жанров по их названиям.

    :param genre_names: Список названий жанров.
    :return: Список идентификаторов жанров.
    """
    query = """
        SELECT genre_id
        FROM genres
        WHERE name = ANY(%(genre_names)s);
    """
    try:
        # Проверка входных данных
        if not isinstance(genre_names, list) or not all(isinstance(name, str) for name in genre_names):
            raise ValueError("Все названия жанров должны быть строками и передаваться в виде списка.")
        
        # Логирование входных данных
        print(f"Ищем жанры: {genre_names}")

        with get_connection() as conn:
            with conn.cursor() as cur:  # Используем стандартный курсор
                # Выполнение запроса
                cur.execute(query, {"genre_names": genre_names})
                result = cur.fetchall()  # Получаем результат в виде списка кортежей

                # Логирование результата
                # Если результат пустой
                if not result:
                    print(f"Жанры не найдены: {genre_names}")
                    return []

                # Преобразование результата в список идентификаторов
                genre_ids = [row[0] for row in result]  # Берем первый элемент каждого кортежа
                print(f"Найденные идентификаторы жанров: {genre_ids}")
                return genre_ids
    except Exception as e:
        # Логирование ошибок
        print(f"Ошибка при выполнении SQL-запроса: {str(e)}")
        raise Exception(f"Ошибка при получении идентификаторов жанров: {str(e)}")

def get_genre_names_by_ids(genre_ids: List[int]) -> List[str]:
    """
    Получает названия жанров по их идентификаторам.

    :param genre_ids: Список идентификаторов жанров.
    :return: Список названий жанров.
    """
    if not genre_ids:
        return []  # Если список пустой, возвращаем пустой список.

    query = """
        SELECT name 
        FROM genres 
        WHERE genre_id = ANY(%(genre_ids)s);
    """
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                # Передаём список как параметр запроса.
                cur.execute(query, {"genre_ids": genre_ids})
                result = cur.fetchall()
                
                # Возвращаем список названий жанров.
                return [row[0] for row in result]
    except Exception as e:
        raise Exception(f"Ошибка при получении названий жанров: {str(e)}")



def filter(title_substr=None, genre_names=None, year_range=None):
    """
    Фильтрует фильмы по заданным критериям: подстроке в названии, жанрам и диапазону лет.

    :param title_substr: Подстрока для поиска в названии фильмов.
    :param genre_names: Список названий жанров.
    :param year_range: Диапазон годов в формате [start_year, end_year].
    :return: Список фильмов с соответствующими критериями, включая названия жанров.
    """
    genre_ids = None
    if genre_names:
        genre_ids = get_genre_ids_by_names(genre_names)  # Получаем genre_ids по именам жанров.

    query = """
        SELECT m.movie_id, m.title, m.year, m.genres
        FROM movies m
        WHERE TRUE
    """
    params = {}

    if title_substr:
        query += " AND LOWER(m.title) LIKE LOWER(%(title_substr)s)"
        params["title_substr"] = f"%{title_substr}%"

    if genre_ids:
        query += " AND m.genres && %(genre_ids)s"
        params["genre_ids"] = genre_ids

    if year_range:
        query += " AND m.year BETWEEN %(start_year)s AND %(end_year)s"
        params["start_year"], params["end_year"] = year_range

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                movies = cur.fetchall()

                # Преобразуем genre_ids в их соответствующие названия.
                movie_results = []
                for movie in movies:
                    movie_id, title, year, genre_ids = movie
                    genre_names = get_genre_names_by_ids(genre_ids)  # Получаем названия жанров.
                    
                    # Формируем результат с названиями жанров вместо genre_ids
                    movie_results.append({
                        "movie_id": movie_id,
                        "title": title,
                        "year": year,
                        "genres": genre_names
                    })

                return movie_results
    except Exception as e:
        raise Exception(f"Ошибка при фильтрации: {str(e)}")

