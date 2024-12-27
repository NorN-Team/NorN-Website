import pandas as pd
import re
from quieries import add_movie

# Загрузка данных
movies = pd.read_csv('C:/Users/ivank/MAI/NorN-Website/BD/dataset/movies.csv')

# Обработка каждой строки
for _, row in movies.iterrows():
    # Разделяем строку на movieId, title и genres
    movieId = row['movieId']
    full_title = row['title']
    genres = row['genres']

    # Выделяем дату из title (если есть)
    match = re.search(r'\((\d{4})\)', full_title)
    if match:
        year = match.group(1)  # Год внутри скобок
        title = full_title[:match.start()].strip()  # Название до скобок
    else:
        year = 1111
        title = full_title.strip()  # Название целиком, если года нет

    # Разделяем жанры по "|"
    genres_list = genres.split('|')

    # Вызываем функцию add_movie
    add_movie(movieId, title, year, genres_list)
