from fastapi import APIRouter, HTTPException
import pickle
import os
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
from models.quieries import get_user_ratings, add_recommendations, get_movie_details  # Импортируем новую функцию для получения деталей фильмов
from joblib import load


router = APIRouter()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Указываем пути к файлам относительно этой директории
RATINGS_PATH = os.path.join(CURRENT_DIR, "ratings.csv")
PKL_PATH = os.path.join(CURRENT_DIR, "similar_movies_dict.pkl")

ratings = pd.read_csv(RATINGS_PATH)

# Загружаем CSV-файл

try:
    similar_movies_dict = load(PKL_PATH)
    print("Файл успешно загружен с помощью joblib!")
except Exception as e:
    print(f"Ошибка при загрузке файла: {e}")



@router.get("/recommendations")
async def get_predictions(userId : int):
    # Получаем оценки пользователя из базы данных
    user_ratings_data = get_user_ratings(userId)

    # Преобразуем данные в DataFrame
    user_ratings = pd.DataFrame(user_ratings_data, columns=['userId', 'movieId', 'rating'])
    user_mean_rating = user_ratings['rating'].mean()

    predictions = []

    # Получаем список уникальных movieId
    movie_ids = ratings['movieId'].unique()
    # Исключаем фильмы, которые пользователь уже оценил
    rated_movie_ids = user_ratings['movieId'].values
    movie_ids_to_predict = [movie_id for movie_id in movie_ids if movie_id not in rated_movie_ids]

    for movie_id in movie_ids_to_predict:
        similar_movies = similar_movies_dict.get(movie_id, [])

        a = 0
        b = 0

        for similar_movie_id, similarity in similar_movies:
            # Проверяем, оценивал ли пользователь похожий фильм
            if similar_movie_id in user_ratings['movieId'].values:
                similar_movie_rating = user_ratings[user_ratings['movieId'] == similar_movie_id]['rating'].values[0]
                rating_diff = similar_movie_rating - user_mean_rating
                a += similarity * rating_diff
                b += similarity

        if b != 0:
            prediction = user_mean_rating + (a / b)
        else:
            prediction = user_mean_rating  # Если нет похожих фильмов, используем среднюю оценку

        predictions.append((movie_id, prediction))

    # Сортируем кортеж по убыванию оценок
    predictions.sort(key=lambda x: x[1], reverse=True)
    top_movie_ids = [movie_id for movie_id, _ in predictions[:10]]

    # Получаем информацию о фильмах
    movie_results = []
    for movie_id in top_movie_ids:
        movie_details = get_movie_details(movie_id)  # Функция для получения данных фильма из базы
        if movie_details:
            movie_results.append({
                "movie_id": movie_details['movie_id'],
                "title": movie_details['title'],
                "year": movie_details['year'],
                "genres": movie_details['genres']
            })

    # Сохраняем рекомендации в базе данных
    add_recommendations(userId, top_movie_ids)

    return movie_results
