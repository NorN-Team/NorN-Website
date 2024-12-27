from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from models.user import User, users  # Импортируем класс User
from services.messaging.producer import send_registration_email

app = FastAPI()
router = APIRouter()

# Определяем Pydantic-модель для входных данных
class RegisterData(BaseModel):
    username: str
    password: str
    email: EmailStr  # Валидация email через Pydantic

@router.post("/register")
def register_user(data: RegisterData):
    username = data.username
    password = data.password
    email = data.email

    # Проверка на уникальность имени пользователя
    if any(user.username == username for user in users):
        raise HTTPException(status_code=400, detail="Имя пользователя уже существует")

    # Проверка на уникальность email
    if any(user.email == email for user in users):
        raise HTTPException(status_code=400, detail="Email уже используется")

    # Генерация нового ID
    new_id = 1 if not users else users[-1].user_id + 1

    # Создание нового пользователя
    new_user = User(user_id=new_id, username=username, email=email, password=password, role="admin")
    users.append(new_user)

    # Отправка уведомления через RabbitMQ
    try:
        send_registration_email(email)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка отправки уведомления: {str(e)}")

    # Возвращаем сообщение и объект пользователя
    return {
        "message": "Пользователь успешно зарегистрирован. Проверьте вашу почту для подтверждения.",
        "user": {"user_id": new_user.user_id, "username": new_user.username}
    }

# Подключаем маршруты
app.include_router(router, tags=["Auth"])
