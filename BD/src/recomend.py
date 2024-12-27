import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import pickle

# Загрузка данных
ratings = pd.read_csv('C:\Users\ivank\MAI\NorN-Website\BD\dataset\ratings.csv')

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


with open("similar_movies_dict.pkl", "wb") as file:
    pickle.dump(similar_movies_dict, file)
