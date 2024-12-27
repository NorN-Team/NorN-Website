from fastapi import APIRouter, HTTPException
from settings import get_connection

router = APIRouter()

@router.get("/")
def get_movies():
    query = "SELECT * FROM movies;"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

@router.get("/movie_page/{movie_id}")
def get_movie(movie_id: int):
    query = "SELECT * FROM movies WHERE movie_id = %(movie_id)s;"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, {"movie_id": movie_id})
            movie = cur.fetchone()
            if not movie:
                raise HTTPException(status_code=404, detail="Фильм не найден")
            return movie