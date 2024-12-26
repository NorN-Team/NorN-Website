# user.py
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from database import SessionLocal

class User(BaseModel):
    username: str = Field(..., min_length=1, description="Имя пользователя должно содержать минимум 1 символ")
    password: str = Field(..., min_length=8, description="Пароль должен содержать минимум 8 символов")

class LoginData(BaseModel):
    username: str
    password: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()