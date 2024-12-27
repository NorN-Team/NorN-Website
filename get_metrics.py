from sklearn.model_selection import KFold
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Загрузка данных
ratings = pd.read_csv('./ratings.csv')

# Создание матрицы рейтингов пользователей для фильмов
movie_user_matrix = ratings.pivot_table(index='movieId', columns='userId', values='rating').fillna(0)

# Расчет косинусовой схожести между фильмами
cosine_sim = cosine_similarity(movie_user_matrix)

# Преобразование в датафрейм для удобства
cosine_sim_df = pd.DataFrame(cosine_sim, index=movie_user_matrix.index, columns=movie_user_matrix.index)

# Предварительный расчет схожести всех фильмов
similar_movies_dict = {}
for movie_id in cosine_sim_df.index:
    similar_movies = cosine_sim_df[movie_id].sort_values(ascending=False).drop(movie_id).head(5)
    similar_movies_dict[movie_id] = list(similar_movies.items())
# Загрузка данных
ratings = pd.read_csv('./ratings.csv')

def test_user(userId):
    # Получаем среднюю оценку, которую пользователь поставил фильмам
    user_ratings = ratings[ratings['userId'] == userId]
    user_mean_rating = user_ratings['rating'].mean()

    predictions = []
    real_ratings = []

    # Проходим только по тем фильмам, которые пользователь оценил
    for movie_id in user_ratings['movieId'].values:
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

        predictions.append(prediction)
        real_ratings.append(user_ratings[user_ratings['movieId'] == movie_id]['rating'].values[0])

    # Вычисляем MAE и RMSE
    mae = mean_absolute_error(real_ratings, predictions)
    rmse = np.sqrt(mean_squared_error(real_ratings, predictions))

    return mae, rmse


def cross_validation(k):
    # Получаем список уникальных userId
    user_ids = ratings['userId'].unique()

    # Создаем KFold объект
    kf = KFold(n_splits=k, shuffle=True, random_state=42)

    fold_mae_scores = []
    fold_rmse_scores = []

    # Разбиваем пользователей на k фолдов
    for train_index, test_index in kf.split(user_ids):
        train_users = user_ids[train_index]
        test_users = user_ids[test_index]

        # Обучаем модель на тренировочном наборе (train_users)
        train_ratings = ratings[ratings['userId'].isin(train_users)]

        # Создание матрицы рейтингов пользователей для фильмов
        movie_user_matrix = train_ratings.pivot_table(index='movieId', columns='userId', values='rating').fillna(0)

        # Расчет косинусовой схожести между фильмами
        cosine_sim = cosine_similarity(movie_user_matrix)

        # Преобразование в датафрейм для удобства
        cosine_sim_df = pd.DataFrame(cosine_sim, index=movie_user_matrix.index, columns=movie_user_matrix.index)

        # Предварительный расчет схожести всех фильмов
        global similar_movies_dict
        similar_movies_dict = {}
        for movie_id in cosine_sim_df.index:
            similar_movies = cosine_sim_df[movie_id].sort_values(ascending=False).drop(movie_id).head(5)
            similar_movies_dict[movie_id] = list(similar_movies.items())

        # Тестируем модель на тестовом наборе (test_users)
        fold_mae = []
        fold_rmse = []

        for user_id in test_users:
            mae, rmse = test_user(user_id)
            fold_mae.append(mae)
            fold_rmse.append(rmse)


        # Сохраняем средние значения MAE и RMSE для текущего фолда
        fold_mae_scores.append(np.mean(fold_mae))
        fold_rmse_scores.append(np.mean(fold_rmse))

    # Вычисляем средние значения MAE и RMSE по всем фолдам
    avg_mae = np.mean(fold_mae_scores)
    avg_rmse = np.mean(fold_rmse_scores)

    return avg_mae, avg_rmse

# Пример использования функции
k = 2  # Замените на нужное количество фолдов
avg_mae, avg_rmse = cross_validation(k)
print(f"Average MAE: {avg_mae}, Average RMSE: {avg_rmse}")


# Создание матрицы рейтингов пользователей для фильмов
movie_user_matrix = ratings.pivot_table(index='movieId', columns='userId', values='rating').fillna(0)

# Расчет косинусовой схожести между фильмами
cosine_sim = cosine_similarity(movie_user_matrix)

# Преобразование в датафрейм для удобства
cosine_sim_df = pd.DataFrame(cosine_sim, index=movie_user_matrix.index, columns=movie_user_matrix.index)

# Предварительный расчет схожести всех фильмов
similar_movies_dict = {}
for movie_id in cosine_sim_df.index:
    similar_movies = cosine_sim_df[movie_id].sort_values(ascending=False).drop(movie_id).head(5)
    similar_movies_dict[movie_id] = list(similar_movies.items())
