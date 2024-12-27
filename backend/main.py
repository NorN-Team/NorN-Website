from fastapi import FastAPI
from endpoints import movies, movie_page, register, login, ratings, recommendations, getrole, add_movie
from fastapi.middleware.cors import CORSMiddleware

# Создание экземпляра FastAPI
app = FastAPI(
    title="Online Cinema API",
    description="API для онлайн-кинотеатра с фильтрацией фильмов по жанрам, годам и названию.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Или укажите конкретный адрес фронтенда, например, ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутов
app.include_router(movies.router, prefix="/movies", tags=["Movies"])
app.include_router(movie_page.router, tags=["Movies"])
app.include_router(register.router, prefix="/auth", tags=["Auth"])
app.include_router(login.router, prefix="/auth", tags=["Auth"])
app.include_router(ratings.router, prefix="/ratings", tags=["Ratings"])
app.include_router(recommendations.router, tags=["ML"])
app.include_router(getrole.router, tags=["Admin"])
app.include_router(add_movie.router, tags=["Admin"])

# Пример корневого эндпоинта
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Добро пожаловать в API онлайн-кинотеатра!"}

# Запуск приложения для локального тестирования
if __name__ == "__main__":
    import uvicorn # type: ignore
    uvicorn.run(app, host="127.0.0.1", port=8000)
