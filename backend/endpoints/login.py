from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from settings import get_connection1

router = APIRouter()

class LoginData(BaseModel):
    username: str
    password: str

@router.post("/login")
def login_user(data: LoginData):
    query = """
        SELECT user_id FROM users
        WHERE user_name = %(username)s AND user_password = %(password)s;
    """
    with get_connection1() as conn:
        with conn.cursor() as cur:
            cur.execute(query, {"username": data.username, "password": data.password})
            user = cur.fetchone()
            if not user:
                raise HTTPException(status_code=401, detail="Неверное имя пользователя или пароль")
            return {"message": "Успешный вход", "user_id": user["user_id"]}
