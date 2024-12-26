from fastapi import FastAPI, Query, APIRouter
from typing import List, Optional
from services.filter import filter  # Убедитесь, что эта функция реализована
from models.movie_structure import Movie, movies

# Создаем экземпляр APIRouter
router = APIRouter()

# Эндпоинт для получения всех фильмов
@router.get("/", response_model=List[Movie])
async def get_movies():
    return movies

# Эндпоинт для получения фильмов с фильтрацией
@router.get("/filter", response_model=List[Movie])
def get_filtered_movies(
    title_substr: Optional[str] = Query(None, description="Подстрока для поиска в названии фильма"),
    genres: Optional[List[str]] = Query(None, description="Список жанров для фильтрации"),
    start_year: Optional[int] = Query(None, description="Начало диапазона лет"),
    end_year: Optional[int] = Query(None, description="Конец диапазона лет")
):
    print(f"title_substr={title_substr}, genres={genres}, start_year={start_year}, end_year={end_year}")
    year_range = (start_year, end_year) if start_year is not None and end_year is not None else None
    return filter(movies, title_substr=title_substr, genres=genres, year_range=year_range)

    """
    Эндпоинт для получения фильмов с фильтрацией по названию, жанрам и диапазону лет.

    :param title_substr: Подстрока, которая должна быть в названии фильма.
    :param genres: Жанры, которые должны быть у фильма.
    :param start_year: Год начала диапазона.
    :param end_year: Год окончания диапазона.
    :return: Отфильтрованный список фильмов.
    """
    year_range = (start_year, end_year) if start_year is not None and end_year is not None else None
    return filter_movies(movies, title_substr=title_substr, genres=genres, year_range=year_range)

# Создаем приложение FastAPI
app = FastAPI()

# Подключаем маршруты
app.include_router(router, prefix="/movies", tags=["Movies"])


