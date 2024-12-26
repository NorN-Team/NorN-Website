from fastapi import FastAPI, APIRouter, HTTPException
from models.movie_structure import Movie, movies  # Убедитесь, что структура `movies` существует

router = APIRouter()

@router.get("/movie_page/{movie_id}", response_model=Movie)  # Измените маршрут на /movies/{movie_id}
async def get_movie(movie_id: int):
    """
    Эндпоинт для получения информации о фильме по его ID.
    """
    # Найти фильм по ID
    for movie in movies:
        if movie.id == movie_id:
            return movie

    # Если фильм не найден, вернуть 404
    raise HTTPException(status_code=404, detail="Фильм не найден")

app = FastAPI()

# Подключаем маршруты
app.include_router(router, tags=["Movies"])