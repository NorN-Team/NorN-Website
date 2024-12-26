from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase, relationship
from uuid import UUID, uuid4
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class Base(DeclarativeBase):
    pass

# Таблица для связи многие-ко-многим между Movie и Genre
movie_genre_association = Table(
    "movie_genre",
    Base.metadata,
    Column("movie_id", UUID, ForeignKey("movie.movie_id"), primary_key=True),
    Column("genre_id", UUID, ForeignKey("genre.genre_id"), primary_key=True),
)

class User(Base):
    __tablename__ = "user"

    user_id = Column(UUID, primary_key=True, default=uuid4)  # Используем UUID для уникального идентификатора
    username = Column(String(32), unique=True, nullable=False)  # Уникальное имя пользователя
    hashed_password = Column(String(128), nullable=False)  # Хэшированный пароль

    # Связь с таблицей Rating
    ratings = relationship("Rating", back_populates="user")

class Movie(Base):
    __tablename__ = "movie"

    movie_id = Column(UUID, primary_key=True, default=uuid4)  # Используем UUID для уникального идентификатора
    title = Column(String(256), unique=True, index=True, nullable=False)  # Уникальное название фильма
    year = Column(Integer, nullable=False)  # Год выпуска фильма

    # Связь с таблицей Rating
    ratings = relationship("Rating", back_populates="movie")

    # Связь с таблицей Genre через ассоциативную таблицу
    genres = relationship("Genre", secondary=movie_genre_association, back_populates="movies")

class Genre(Base):
    __tablename__ = "genre"

    genre_id = Column(UUID, primary_key=True, default=uuid4)  # Используем UUID для уникального идентификатора
    name = Column(String(50), unique=True, nullable=False)  # Название жанра

    # Связь с таблицей Movie через ассоциативную таблицу
    movies = relationship("Movie", secondary=movie_genre_association, back_populates="genres")

class Rating(Base):
    __tablename__ = "rating"

    score_id = Column(UUID, primary_key=True, default=uuid4)  # Используем UUID для уникального идентификатора
    score = Column(Integer, nullable=False)  # Оценка фильма
    movie_id = Column(UUID, ForeignKey("movie.movie_id"), nullable=False)  # Связь с таблицей Movie
    user_id = Column(UUID, ForeignKey("user.user_id"), nullable=False)  # Связь с таблицей User

    # Связи с таблицами User и Movie
    user = relationship("User", back_populates="ratings")
    movie = relationship("Movie", back_populates="ratings")

# Функция для загрузки данных из CSV
def load_movies_from_csv(csv_file: str):
    # Подключение к базе данных
    DATABASE_URL = "sqlite:///movies.db"  # Используйте свою строку подключения
    engine = create_engine(DATABASE_URL)

    # Создание таблиц в базе данных (если их нет)
    Base.metadata.create_all(bind=engine)

    # Чтение CSV-файла
    df = pd.read_csv(csv_file)

    # Создание сессии
    with Session(engine) as session:
        # Словарь для хранения жанров (чтобы избежать дублирования)
        genres_dict = {}

        # Обработка каждой строки в CSV
        for index, row in df.iterrows():
            # Извлечение данных
            movie_id = uuid4()  # Генерация UUID для фильма
            title = row["title"]
            year = int(title.split("(")[-1].strip(")"))  # Извлечение года из названия
            genres = row["genres"].split("|")  # Разделение жанров

            # Создание записи фильма
            movie = Movie(movie_id=movie_id, title=title, year=year)
            session.add(movie)

            # Обработка жанров
            for genre_name in genres:
                # Если жанр уже существует, используем его
                if genre_name in genres_dict:
                    genre = genres_dict[genre_name]
                else:
                    # Создаем новый жанр
                    genre = Genre(genre_id=uuid4(), name=genre_name)
                    session.add(genre)
                    genres_dict[genre_name] = genre

                # Создаем связь между фильмом и жанром
                session.execute(movie_genre_association.insert().values(movie_id=movie.movie_id, genre_id=genre.genre_id))

        # Сохранение изменений в базе данных
        session.commit()

# Пример использования
if __name__ == "__main__":
    load_movies_from_csv("movies.csv")

# Пример данных фильмов
movies = [
    Movie(id = 1, title="Toy Story (1995)", year=1995, genres=["Adventure", "Animation", "Children", "Comedy", "Fantasy"]),
    Movie(id = 2, title="The Matrix (1999)", year=1999, genres=["Action", "Sci-Fi", "Thriller"]),
    Movie(id = 3, title="Inception (2010)", year=2010, genres=["Action", "Adventure", "Sci-Fi"]),
    Movie(id = 4, title="Spirited Away (2001)", year=2001, genres=["Animation", "Adventure", "Fantasy"]),
    Movie(id = 5, title="The Dark Knight (2008)", year=2008, genres=["Action", "Crime", "Drama"]),
    Movie(id = 6, title="Forrest Gump (1994)", year=1994, genres=["Drama", "Romance"]),
    Movie(id = 7, title="The Lion King (1994)", year=1994, genres=["Animation", "Adventure", "Drama"]),
    Movie(id = 8, title="Pulp Fiction (1994)", year=1994, genres=["Crime", "Drama"]),
    Movie(id = 9, title="The Shawshank Redemption (1994)", year=1994, genres=["Drama"]),
    Movie(id = 10, title="Avengers: Endgame (2019)", year=2019, genres=["Action", "Adventure", "Drama"]),
]