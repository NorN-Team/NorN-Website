from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from settings import get_connection

router = APIRouter()

class RatingData(BaseModel):
    user_id: int
    movie_id: int
    rating: float

@router.post("/rate_movie")
def rate_movie(data: RatingData):
    if not (0.5 <= data.rating <= 5.0):
        raise HTTPException(status_code=400, detail="Оценка должна быть от 0.5 до 5.0")

    query = """
        INSERT INTO ratings (user_id, movie_id, rating)
        VALUES (%(user_id)s, %(movie_id)s, %(rating)s)
        ON CONFLICT (user_id, movie_id)
        DO UPDATE SET rating = EXCLUDED.rating;
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, {
                "user_id": data.user_id,
                "movie_id": data.movie_id,
                "rating": data.rating
            })
            conn.commit()
            return {"message": "Оценка успешно сохранена"}
