import React, { useEffect, useState } from "react";
import { useParams, useNavigate, useLocation } from "react-router-dom";
import "./MoviePage.css";

const MoviePage = () => {
  const { id } = useParams(); // Получаем id из URL
  const location = useLocation(); // Получаем location для доступа к state
  const { userId } = location.state || {}; // Извлекаем userId из state
  const navigate = useNavigate();
  const [data, setMovie] = useState(null);
  const [loading, setLoading] = useState(true);
  const [rating, setRating] = useState(3);
  const [successMessage, setSuccessMessage] = useState("");

  const turnBack = () => {
    navigate("/main", { state: { userId } }); // Передаем userId обратно
  };

  useEffect(() => {
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
          movie_id: data[0],
          user_id: userId, // Используем userId
          rating,
        }),
      });

      if (!response.ok) {
        throw new Error("Ошибка отправки оценки");
      }

      setSuccessMessage("Оценка успешно отправлена!");
      setTimeout(() => setSuccessMessage(""), 5000);
    } catch (error) {
      console.error("Ошибка:", error);
    }
  };

  if (loading) return <p className="loading-message">Загрузка...</p>;
  if (!data) return <p className="not-found-message">Фильм не найден</p>;

  return (
    <div className="movie-page-container">
      <div className="movie-header">{data[1]}</div>
      <div className="movie-details">
        <div className="movie-detail-item">Год выпуска в прокат: {data[2]}</div>
        <div className="movie-detail-item movie-genres">
          Жанры: {data[3]}
        </div>
        <div className="movie-detail-item movie-description">
          Описание:
        </div>
      </div>
      <div className="rating-container">
        <h3>Оценить фильм</h3>
        <input
          type="range"
          className="rating-slider"
          min="0.5"
          max="5.0"
          step="0.5" // Устанавливаем шаг изменения
          value={rating}
          onChange={(e) => setRating(Number(e.target.value))}
        />
        <span className="rating-value">{rating.toFixed(1)}</span> {/* Отображаем с 1 цифрой после запятой */}
        <button className="rating-button" onClick={handleRatingSubmit}>
          Оценить
        </button>
        <button className="back-button" onClick={turnBack}>
          Назад
        </button>
      </div>
      {successMessage && (
        <div className="success-message">{successMessage}</div>
      )}
    </div>
  );
};

export default MoviePage;