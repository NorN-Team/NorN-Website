from pydantic import BaseModel
from typing import List

# Определение Pydantic-модели для фильма
class Movie(BaseModel):
    title: str
    year: int
    genres: List[str]

# Пример данных фильмов
movies = [
    Movie(title="Toy Story (1995)", year=1995, genres=["Adventure", "Animation", "Children", "Comedy", "Fantasy"]),
    Movie(title="The Matrix (1999)", year=1999, genres=["Action", "Sci-Fi", "Thriller"]),
    Movie(title="Inception (2010)", year=2010, genres=["Action", "Adventure", "Sci-Fi"]),
    Movie(title="Spirited Away (2001)", year=2001, genres=["Animation", "Adventure", "Fantasy"]),
    Movie(title="The Dark Knight (2008)", year=2008, genres=["Action", "Crime", "Drama"]),
    Movie(title="Forrest Gump (1994)", year=1994, genres=["Drama", "Romance"]),
    Movie(title="The Lion King (1994)", year=1994, genres=["Animation", "Adventure", "Drama"]),
    Movie(title="Pulp Fiction (1994)", year=1994, genres=["Crime", "Drama"]),
    Movie(title="The Shawshank Redemption (1994)", year=1994, genres=["Drama"]),
    Movie(title="Avengers: Endgame (2019)", year=2019, genres=["Action", "Adventure", "Drama"]),
]
