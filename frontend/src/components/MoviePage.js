import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import "./MoviePage.css";

const MoviePage = () => {
  const { id } = useParams(); // Получаем id из URL
  const [movie, setMovie] = useState(null);
  const [loading, setLoading] = useState(true);
  const [rating, setRating] = useState(3); // Значение ползунка по умолчанию
  const [successMessage, setSuccessMessage] = useState(""); // Сообщение об успехе

  useEffect(() => {
    // Фетчим информацию о фильме с сервера
    const fetchMovie = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/movie_page/${id}`);
        if (!response.ok) {
          throw new Error("Ошибка загрузки данных фильма");
        }
        const data = await response.json();
        setMovie(data);
      } catch (error) {
        console.error("Ошибка:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchMovie();
  }, [id]);

  const handleRatingSubmit = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/ratings/rate_movie`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          film_id: id,
          user_id: 1, // Здесь можно использовать ID авторизованного пользователя
          rating,
        }),
      });

      if (!response.ok) {
        throw new Error("Ошибка отправки оценки");
      }

      setSuccessMessage("Оценка успешно отправлена!"); // Устанавливаем сообщение об успехе

      // Очищаем сообщение через 5 секунд
      setTimeout(() => setSuccessMessage(""), 5000);
    } catch (error) {
      console.error("Ошибка:", error);
    }
  };

  if (loading) return <p className="loading-message">Загрузка...</p>;
  if (!movie) return <p className="not-found-message">Фильм не найден</p>;

  return (
    <div className="movie-page-container">
      <div className="movie-header">{movie.title}</div>
      <div className="movie-details">
        <div className="movie-detail-item">Год выпуска в прокат: {movie.year}</div>
        <div className="movie-detail-item movie-genres">
          Жанры: {movie.genres.join(", ")}
        </div>
        <div className="movie-detail-item movie-description">
          Описание: {movie.description}
        </div>
      </div>
      <div className="rating-container">
        <h3>Оценить фильм</h3>
        <input
          type="range"
          className="rating-slider"
          min="1"
          max="5"
          value={rating}
          onChange={(e) => setRating(Number(e.target.value))}
        />
        <span className="rating-value">{rating}</span>
        <button className="rating-button" onClick={handleRatingSubmit}>
          Оценить
        </button>
      </div>
      {successMessage && ( // Условный рендеринг сообщения об успехе
        <div className="success-message">{successMessage}</div>
      )}
    </div>
  );
};

export default MoviePage;
