from pydantic import BaseModel, Field

# Класс User для модели данных
class User(BaseModel):
    user_id: int
    username: str = Field(..., min_length=1, description="Имя пользователя должно содержать минимум 1 символ")
    email: str
    password: str = Field(..., min_length=8, description="Пароль должен содержать минимум 8 символов")
    role: str

# Временное хранилище пользователей
users = []