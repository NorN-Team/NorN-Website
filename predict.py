import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
from repositories.actions import get_user_ratings, add_recommendations

ratings = pd.read_csv('./dataset/ratings.csv')

with open("similar_movies_dict.pkl", "rb") as file:
  similar_movies_dict = pickle.load(file)


def get_predictions(userId):
    # Получаем среднюю оценку, которую пользователь поставил фильмам
#    user_ratings = ratings[ratings['userId'] == userId]
#    user_ratings = get_user_ratings(userId)
    # Получаем оценки пользователя из базы данных
    user_ratings_data = get_user_ratings(userId)

    # Преобразуем данные в DataFrame
    user_ratings = pd.DataFrame(user_ratings_data, columns=['userId', 'movieId', 'rating'])
#    print(user_ratings.head())
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
    recommendations = [movie_id for movie_id, _ in predictions[:10]]
    recommendations = [int(movie_id) for movie_id in recommendations]
    add_recommendations(userId, recommendations)
    return recommendations
