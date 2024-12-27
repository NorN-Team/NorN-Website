from fastapi import FastAPI, Query, APIRouter, HTTPException
from typing import List, Optional
from services.filter import filter  # Обновленная функция фильтрации

router = APIRouter()

from fastapi.logger import logger

@router.get("/filter", response_model=List[dict])
def get_filtered_movies(
    title_substr: Optional[str] = Query(None, description="Подстрока для поиска в названии фильма"),
    genres: Optional[List[str]] = Query(None, description="Список жанров для фильтрации"),
    start_year: Optional[int] = Query(None, description="Начало диапазона лет"),
    end_year: Optional[int] = Query(None, description="Конец диапазона лет")
):
    try:
        year_range = (start_year, end_year) if start_year is not None and end_year is not None else None
        filtered_movies = filter(title_substr=title_substr, genre_names=genres, year_range=year_range)
        return filtered_movies
    except Exception as e:
        logger.error(f"Ошибка фильтрации фильмов: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Ошибка фильтрации фильмов: {str(e)}")
