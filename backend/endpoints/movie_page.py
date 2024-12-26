# movie_page.py
from fastapi import FastAPI, APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.movie_structure import Movie as MovieModel
from models.movie_structure import Movie
from models.user import get_db

router = APIRouter()

@router.get("/movie_page/{movie_id}", response_model=Movie)
async def get_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Фильм не найден")
    return db_movie

app = FastAPI()

# Подключаем маршруты
app.include_router(router, tags=["Movies"])