from fastapi import APIRouter, HTTPException
from models.user import users  # Импортируйте список пользователей

router = APIRouter()

@router.get("/user-role")
async def get_user_role(user_id: int):
    try:
        # Найти пользователя по user_id
        user = next((u for u in users if u.user_id == user_id), None)
        
        # Если пользователь не найден
        if not user:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        
        # Возвращаем роль пользователя
        return {"role": user.role}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")
