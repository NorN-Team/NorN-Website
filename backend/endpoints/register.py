from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from models.user import User, users  # Импортируем класс User

app = FastAPI()
router = APIRouter()

# Определяем Pydantic-модель для входных данных
class RegisterData(BaseModel):
    username: str
    password: str

@router.post("/register")
def register_user(data: RegisterData):
    username = data.username
    password = data.password

    # Проверка на уникальность имени пользователя
    if any(user.username == username for user in users):
        raise HTTPException(status_code=400, detail="Имя пользователя уже существует")

    # Генерация нового ID
    new_id = 1 if not users else users[-1].user_id + 1

    # Создание нового пользователя
    new_user = User(user_id=new_id, username=username, password=password)
    users.append(new_user)

    # Возвращаем сообщение и объект пользователя
    return {"message": "Пользователь успешно зарегистрирован", "user": {"user_id": new_user.user_id, "username": new_user.username}}

# Подключаем маршруты
app.include_router(router, tags=["Auth"])
