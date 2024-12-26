from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from models.user import User, users  # Импортируем класс User

app = FastAPI()
router = APIRouter()

# Определяем Pydantic-модель для входных данных
class LoginData(BaseModel):
    username: str
    password: str

@router.post("/login")
def register_user(data: LoginData):
    for user in users:
        if user.username == data.username and user.password == data.password:
            return {"message": "Успешный вход", "user": {"user_id": user.user_id}}

    raise HTTPException(status_code=401, detail="Неверное имя пользователя или пароль")

# Подключаем маршруты
app.include_router(router, tags=["Auth"])
