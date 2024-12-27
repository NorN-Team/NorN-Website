import psycopg2
from psycopg2.extras import RealDictCursor
from repositories.connector import get_connection


def add_movie(movieId: int, title: str, date: str, genres: list[str]):
    # SQL-запросы
    get_genres_query = """
        SELECT genre_id, name
        FROM genres;
    """
    insert_genre_query = """
        INSERT INTO genres (name)
        VALUES (%(name)s)
        RETURNING genre_id;
    """
    insert_movie_query = """
        INSERT INTO movies (movie_id, title, year, genres)
        VALUES (%(movie_id)s, %(title)s, %(year)s, %(genres)s);
    """

    # Открытие соединения и выполнение запросов
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            # Получаем все существующие жанры
            cur.execute(get_genres_query)
            existing_genres = {row["name"]: row["genre_id"] for row in cur.fetchall()}  # {name: genre_id}

            genre_ids = []
            for genre in genres:
                if genre in existing_genres:
                    genre_ids.append(existing_genres[genre])
                else:
                    # Добавляем новый жанр, если его нет
                    cur.execute(insert_genre_query, {"name": genre})
                    new_genre_id = cur.fetchone()["genre_id"]  # Используем ключ вместо индекса
                    genre_ids.append(new_genre_id)
                    existing_genres[genre] = new_genre_id

            # Преобразуем год из строки даты
            year = int(date)  # Предполагаем формат "1995"

            # Добавляем фильм
            cur.execute(insert_movie_query, {
                "movie_id": movieId,
                "title": title,
                "year": year,
                "genres": genre_ids
            })

            # Фиксация изменений
            conn.commit()



def get_user_ratings(userId: int):
    query = """
        SELECT user_id, movie_id, rating
        FROM ratings
        WHERE user_id = %(user_id)s;
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, {"user_id": userId})
            return cur.fetchall()

from typing import Dict
from repositories.settings import get_connection  # Предполагается, что подключение к базе настроено

def get_movie_details(movie_id: int) -> Dict:
    """
    Получает детали фильма из базы данных по его ID.

    :param movie_id: ID фильма.
    :return: Словарь с информацией о фильме.
    """
    query = """
        SELECT movie_id, title, year, genres
        FROM movies
        WHERE movie_id = %s;
    """
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (movie_id,))
                result = cur.fetchone()
                if result:
                    return {
                        "movie_id": result[0],
                        "title": result[1],
                        "year": result[2],
                        "genres": result[3].split(", ")  # Если жанры хранятся как строка
                    }
                return None
    except Exception as e:
        raise Exception(f"Ошибка при получении информации о фильме: {str(e)}")

def add_recommendations(userId: int, recommendations: list[int]):
    query = """
        UPDATE users
        SET recommendations = %(recommendations)s
        WHERE user_id = %(user_id)s;
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, {
                "user_id": userId,
                "recommendations": recommendations
            })
            conn.commit()
