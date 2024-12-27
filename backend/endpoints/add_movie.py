from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from models.movie_structure import movies, Movie
from typing import List

router = APIRouter()

class MovieInput(BaseModel):
    title: str = Field(..., min_length=1, description="Название фильма")
    year: int = Field(..., description="Год выпуска (целое число)")
    genres: List[str] = Field(..., description="Жанры в виде списка строк")

@router.post("/add-movie")
async def add_movie(movie_input: MovieInput):
    print(f"Полученные данные: {movie_input}")
    # Проверка существования фильма
    if any(existing_movie for existing_movie in movies if existing_movie.title.lower() == movie_input.title.lower()):
        raise HTTPException(status_code=400, detail="Фильм с таким названием уже существует")

    # Генерируем новый ID
    new_id = 1 if not movies else movies[-1].id + 1

    # Создаем новый фильм
    new_movie = Movie(
        id=new_id,
        title=movie_input.title,
        year=movie_input.year,
        genres=movie_input.genres
    )
    movies.append(new_movie)

    return {"message": "Фильм успешно добавлен", "movie": new_movie}

