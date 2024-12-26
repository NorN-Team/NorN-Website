# login.py
from fastapi import FastAPI, APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.user import User as UserModel
from models.user import LoginData, get_db

router = APIRouter()

@router.post("/login")
async def login(data: LoginData, db: Session = Depends(get_db)):
    # Проверяем пользователя в базе данных
    db_user = db.query(UserModel).filter(UserModel.username == data.username, UserModel.password == data.password).first()
    if db_user:
        return {"message": "Успешный вход"}
    raise HTTPException(status_code=401, detail="Неверное имя пользователя или пароль")

app = FastAPI()

# Подключаем маршруты
app.include_router(router, tags=["Auth"])