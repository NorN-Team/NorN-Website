import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "./SearchResults.css";

const Recommendations = ({ userId }) => {
  const [recommendations, setRecommendations] = useState([]); // Рекомендации
  const [loading, setLoading] = useState(true); // Статус загрузки
  const [error, setError] = useState(null); // Ошибка

  useEffect(() => {
    const fetchRecommendations = async () => {
      try {
        console.log(`Запрос к серверу с user_id=${userId}`);
        const response = await fetch(
          `http://127.0.0.1:8000/recommendations?user_id=${userId}`
        );

        if (!response.ok) {
          throw new Error("Ошибка загрузки рекомендаций");
        }

        const data = await response.json();
        console.log("Полученные данные:", data);

        // Преобразуем объект в массив, если необходимо
        const recommendationsArray = Array.isArray(data) ? data : [data];

        if (!recommendationsArray.length) {
          console.warn("Рекомендации пусты.");
        }

        setRecommendations(recommendationsArray);
      } catch (error) {
        console.error("Ошибка:", error);
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchRecommendations();
  }, [userId]);

  if (loading) return <p>Загрузка рекомендаций...</p>;
  if (error) return <p>Ошибка: {error}</p>;
  if (!recommendations.length) return <p className="recommendations-empty">Нет рекомендаций</p>;

  return (
    <div className="search-results-container">
      <h3 className="search-results-title">Рекомендации для вас</h3>
      <div className="search-results-list">
        {recommendations.length > 0 ? (
          recommendations.map((movie) => (
            <div className="search-results-item" key={movie.movie_id}>
              <div className="search-results-poster">Постер</div>
              <div className="search-results-item-content">
                <h4 className="search-results-item-title">
                  <Link 
                    to={`/movies/${movie.movie_id}`}
                    state={{ userId: userId }} // Передаем userId
                  >
                    {movie.title}
                  </Link>
                </h4>
                <p className="search-results-item-genres">
                  Жанры: {movie.genres.join(", ")}
                </p>
              </div>
            </div>
          ))
        ) : (
          <p className="search-results-empty">
            Нет фильмов, соответствующих критериям.
          </p>
        )}
      </div>
    </div>
  );
};

export default Recommendations;
