import os
import psycopg2
from psycopg2.extras import RealDictCursor

# Получаем строку подключения из переменной окружения
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:12345678@localhost:5432/postgres")

def get_connection():
    """
    Создает подключение к базе данных на основе строки подключения.
    """
    try:
        conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
        return conn
    except Exception as e:
        raise Exception(f"Не удалось подключиться к базе данных: {str(e)}")