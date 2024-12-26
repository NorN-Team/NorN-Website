import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import "./MoviePage.css"; // Импорт стилей

const MoviePage = () => {
  const { id } = useParams(); // Получаем id из URL
  const [movie, setMovie] = useState(null);
  const [loading, setLoading] = useState(true);

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

  if (loading) return <p className="loading-message">Загрузка...</p>;
  if (!movie) return <p className="not-found-message">Фильм не найден</p>;

  return (
    <div className="movie-page-container">
      <div className="movie-header">{movie.title}</div>
      <div className="movie-details">
        <div className="movie-detail-item">Год: {movie.year}</div>
        <div className="movie-detail-item movie-genres">
          Жанры: {movie.genres.join(", ")}
        </div>
        <div className="movie-detail-item movie-description">
          Описание: {movie.description}
        </div>
      </div>
    </div>
  );
};

export default MoviePage;
