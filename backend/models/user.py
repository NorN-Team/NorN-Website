from pydantic import BaseModel, Field

# Класс User для модели данных
class User(BaseModel):
    username: str = Field(..., min_length=1, description="Имя пользователя должно содержать минимум 1 символ")
    password: str = Field(..., min_length=8, description="Пароль должен содержать минимум 8 символов")

# Временное хранилище пользователей
users = []