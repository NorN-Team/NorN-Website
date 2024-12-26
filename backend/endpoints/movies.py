from fastapi import FastAPI, Query, APIRouter, Depends
from typing import List, Optional
from sqlalchemy.orm import Session
from models.movie_structure import MovieDB, Genre, movie_genre_association  # Импортируем модели SQLAlchemy
from services.filter import get_db  # Функция для получения сессии базы данных

# Создаем экземпляр APIRouter
router = APIRouter()

# Эндпоинт для получения всех фильмов
@router.get("/", response_model=List[MovieDB])
async def get_movies(db: Session = Depends(get_db)):
    """
    Эндпоинт для получения всех фильмов.
    """
    return db.query(MovieDB).all()

# Эндпоинт для получения фильмов с фильтрацией
@router.get("/filter", response_model=List[MovieDB])
def get_filtered_movies(
    title_substr: Optional[str] = Query(None, description="Подстрока для поиска в названии фильма"),
    genres: Optional[List[str]] = Query(None, description="Список жанров для фильтрации"),
    start_year: Optional[int] = Query(None, description="Начало диапазона лет"),
    end_year: Optional[int] = Query(None, description="Конец диапазона лет"),
    db: Session = Depends(get_db)
):
    """
    Эндпоинт для получения фильмов с фильтрацией по названию, жанрам и диапазону лет.

    :param title_substr: Подстрока, которая должна быть в названии фильма.
    :param genres: Жанры, которые должны быть у фильма.
    :param start_year: Год начала диапазона.
    :param end_year: Год окончания диапазона.
    :param db: Сессия базы данных.
    :return: Отфильтрованный список фильмов.
    """
    # Начинаем с базового запроса
    query = db.query(MovieDB)

    # Фильтрация по подстроке в названии
    if title_substr:
        query = query.filter(MovieDB.title.ilike(f"%{title_substr}%"))

    # Фильтрация по диапазону лет
    if start_year is not None and end_year is not None:
        query = query.filter(MovieDB.year.between(start_year, end_year))

    # Фильтрация по жанрам
    if genres:
        query = query.join(movie_genre_association).join(Genre).filter(Genre.name.in_(genres))

    # Выполняем запрос и возвращаем результат
    return query.all()

# Создаем приложение FastAPI
app = FastAPI()

# Подключаем маршруты
app.include_router(router, prefix="/movies", tags=["Movies"])

# Пример запуска сервера
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)