from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from settings import get_connection1

router = APIRouter()

class RegisterData(BaseModel):
    username: str
    password: str
    email: str

@router.post("/register")
def register_user(data: RegisterData):
    query = """
        INSERT INTO users (user_name, user_password, email, user_role)
        VALUES (%(username)s, %(password)s, %(email)s, 'user')
        RETURNING user_id;
    """
    try:
        with get_connection1() as conn:
            with conn.cursor() as cur:
                cur.execute(query, {
                    "username": data.username,
                    "password": data.password,
                    "email": data.email
                })
                user_id = cur.fetchone()["user_id"]
                conn.commit()
                return {"message": "Пользователь успешно зарегистрирован", "user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка при регистрации: {str(e)}")
