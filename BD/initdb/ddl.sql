CREATE TABLE genres (
    genre_id  SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE movies (
    movie_id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    genres INT[]
);

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,                 -- Уникальный идентификатор пользователя
    user_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    user_role VARCHAR(255) NOT NULL;
    user_password VARCHAR(255) NOT NULL,
    recommendations INT[] DEFAULT '{}'         -- Массив рекомендованных фильмо
);

CREATE TABLE ratings (
    movie_id INT NOT NULL,
    user_id INT NOT NULL,
    rating INT CHECK (rating >= 0 AND rating <= 5),
    PRIMARY KEY (movie_id, user_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
