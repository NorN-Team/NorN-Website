from typing import List
from settings import get_connection

def get_genre_names_by_ids(genre_ids: List[int]) -> List[str]:
    """
    Получает названия жанров по их идентификаторам.

    :param genre_ids: Список идентификаторов жанров.
    :return: Список названий жанров.
    """
    query = """
        SELECT name
        FROM genres
        WHERE genre_id = ANY(%(genre_ids)s);
    """
    
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, {"genre_ids": genre_ids})
                result = cur.fetchall()
                return [row[0] for row in result]  # Извлекаем названия жанров
    except Exception as e:
        raise Exception(f"Ошибка при получении жанров: {str(e)}")
