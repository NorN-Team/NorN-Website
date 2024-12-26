from typing import List
from models.movie_structure import Movie, movies

def recommend(
    user_id: int,
    movies: List[Movie],
) -> List[Movie]:
    
    reccomended = movies[user_id % 10]

    return reccomended

