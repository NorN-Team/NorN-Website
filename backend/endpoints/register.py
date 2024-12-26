from fastapi import FastAPI, APIRouter, HTTPException
from models.user import User, users  # Импортируем класс User

router = APIRouter()

@router.post("/register")
async def register_user(data: User):
    # Проверяем, существует ли пользователь
    for user in users:
        if user["username"] == data.username:
            raise HTTPException(status_code=400, detail="Username уже используется.")

    # Добавляем нового пользователя
    users.append({"username": data.username, "password": data.password})
    return {"message": "Регистрация успешна!"}


app = FastAPI()

# Подключаем маршруты
app.include_router(router, tags=["Auth"])