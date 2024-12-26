# movies.py
from fastapi import FastAPI, Query, APIRouter, Depends
from typing import List, Optional
from sqlalchemy.orm import Session
from models.models import Movie as MovieModel, Genre
from models.movie_structure import Movie
from models.user import get_db

router = APIRouter()

@router.get("/", response_model=List[Movie])
async def get_movies(db: Session = Depends(get_db)):
    return db.query(MovieModel).all()

@router.get("/filter", response_model=List[Movie])
def get_filtered_movies(
    title_substr: Optional[str] = Query(None, description="Substring for movie title search"),
    genres: Optional[List[str]] = Query(None, description="List of genres for filtering"),
    start_year: Optional[int] = Query(None, description="Start year of the range"),
    end_year: Optional[int] = Query(None, description="End year of the range"),
    db: Session = Depends(get_db)
):
    query = db.query(MovieModel)

    if title_substr:
        query = query.filter(MovieModel.title.contains(title_substr))
    if genres:
        query = query.join(MovieModel.genres).filter(Genre.name.in_(genres))
    if start_year and end_year:
        query = query.filter(MovieModel.year.between(start_year, end_year))

    return query.all()

app = FastAPI()

# Подключаем маршруты
app.include_router(router, prefix="/movies", tags=["Movies"])