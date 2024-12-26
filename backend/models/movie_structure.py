from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase, relationship
from uuid import UUID, uuid4

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