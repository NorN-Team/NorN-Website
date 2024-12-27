from fastapi import APIRouter, HTTPException, Query
from settings import get_connection  # Функция для подключения к базе данных

router = APIRouter()

@router.get("/user-role")
async def get_user_role(user_id: int = Query(..., description="ID пользователя")):
    """
    Получает роль пользователя по его ID.
    
    :param user_id: Идентификатор пользователя.
    :return: Роль пользователя.
    """
    try:
        # SQL-запрос для получения пользователя по ID
        query = "SELECT role FROM users WHERE user_id = %(user_id)s"
        params = {"user_id": user_id}

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                result = cur.fetchone()
        
        # Если пользователь не найден
        if not result:
            raise HTTPException(status_code=404, detail="Пользователь не найден")

        # Возвращаем роль пользователя
        return {"role": result[0]}
    
    except Exception as e:
        # Обработка ошибок подключения или запроса
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")
