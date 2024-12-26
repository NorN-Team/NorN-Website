# endpoints/ratings.py
from fastapi import APIRouter, HTTPException
from models.userratings import UserRating, ratings

router = APIRouter()

@router.post("/rate_movie")
async def rate_movie(rating: UserRating):
    # Проверяем, что оценка находится в пределах 1-5
    if not (1 <= rating.rating <= 5):
        raise HTTPException(status_code=400, detail="Оценка должна быть от 1 до 5")
    
    # Проверяем, есть ли уже оценка от этого пользователя для этого фильма
    existing_rating = next((r for r in ratings if r.film_id == rating.film_id and r.user_id == rating.user_id), None)
    if existing_rating:
        # Обновляем существующую оценку
        existing_rating.rating = rating.rating
    else:
        # Добавляем новую оценку
        ratings.append(rating)
    
    return {"message": "Оценка успешно сохранена", "rating": rating}
