# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints import movies, movie_page, register, login

app = FastAPI(
    title="Online Cinema API",
    description="API для онлайн-кинотеатра с фильтрацией фильмов по жанрам, годам и названию.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутов
app.include_router(movies.router, prefix="/movies", tags=["Movies"])
app.include_router(movie_page.router, tags=["Movies"])
app.include_router(register.router, prefix="/auth", tags=["Auth"])
app.include_router(login.router, prefix="/auth", tags=["Auth"])

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Добро пожаловать в API онлайн-кинотеатра!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)