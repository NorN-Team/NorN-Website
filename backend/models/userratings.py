from pydantic import BaseModel
from typing import List

# Модель для хранения оценок
class UserRating(BaseModel):
    film_id: int
    user_id: int
    rating: float  # Число от 0.5 до 5

# Хранилище оценок (для демонстрации)
ratings: List[UserRating] = []
