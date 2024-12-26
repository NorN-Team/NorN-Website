# movie_structure.py
from pydantic import BaseModel
from typing import List

class Movie(BaseModel):
    id: int
    title: str
    year: int
    genres: List[str]

    class Config:
        orm_mode = True