from pydantic import BaseModel
from typing import List

# Определение Pydantic-модели для фильма
class Movie(BaseModel):
    id: int
    title: str
    year: int
    genres: List[str]

# Пример данных фильмов
movies = [
    Movie(id = 1, title="Toy Story (1995)", year=1995, genres=["Adventure", "Animation", "Children", "Comedy", "Fantasy"]),
    Movie(id = 2, title="The Matrix (1999)", year=1999, genres=["Action", "Sci-Fi", "Thriller"]),
    Movie(id = 3, title="Inception (2010)", year=2010, genres=["Action", "Adventure", "Sci-Fi"]),
    Movie(id = 4, title="Spirited Away (2001)", year=2001, genres=["Animation", "Adventure", "Fantasy"]),
    Movie(id = 5, title="The Dark Knight (2008)", year=2008, genres=["Action", "Crime", "Drama"]),
    Movie(id = 6, title="Forrest Gump (1994)", year=1994, genres=["Drama", "Romance"]),
    Movie(id = 7, title="The Lion King (1994)", year=1994, genres=["Animation", "Adventure", "Drama"]),
    Movie(id = 8, title="Pulp Fiction (1994)", year=1994, genres=["Crime", "Drama"]),
    Movie(id = 9, title="The Shawshank Redemption (1994)", year=1994, genres=["Drama"]),
    Movie(id = 10, title="Avengers: Endgame (2019)", year=2019, genres=["Action", "Adventure", "Drama"]),
]
