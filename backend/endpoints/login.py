from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from models.user import User, users  # Импортируем класс User
from typing import List

router = APIRouter()

# Пример массива пользователей

class LoginData(BaseModel):
    username: str
    password: str

@router.post("/login")
async def login(data: LoginData):
    # Проверяем пользователя в списке users
    for user in users:
        if user["username"] == data.username and user["password"] == data.password:
            return {"message": "Успешный вход"}
    raise HTTPException(status_code=401, detail="Неверное имя пользователя или пароль")

app = FastAPI()

# Подключаем маршруты
app.include_router(router, tags=["Auth"])