from fastapi import APIRouter, HTTPException
from models.userratings import ratings  # Импортируем оценки
from models.movie_structure import movies  # Импортируем данные о фильмах
from services.recommendation_service import recommend

router = APIRouter()

@router.get("/recommendations")
async def rate_movie(user_id: int):
    if not user_id:
        raise HTTPException(status_code=400, detail="вы не вошли")

    return recommend(user_id, movies)
