import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "./Recommendations.css";

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
    <div className="recommendations-container">
      <h3 className="recommendations-title">Рекомендации для вас</h3>
      <div className="recommendations-list">
        {recommendations.map((movie) => (
          <div key={movie.id} className="recommendations-item">
            <div
              className="recommendations-poster"
              style={{
                backgroundImage: movie.poster ? `url(${movie.poster})` : "none",
                backgroundSize: "cover",
                backgroundPosition: "center",
              }}
            >
              {!movie.poster && "Постер"}
            </div>
            <div className="recommendations-item-content">
              <h4 className="recommendations-item-title">
                <Link 
                    to={`/movies/${movie.id}`}
                    state={{ userId: userId }} // Передаем userId
                >
                {movie.title}
                </Link>
              </h4>
              <p className="recommendations-item-genres">
                Жанр: {movie.genres && movie.genres.length ? movie.genres.join(", ") : "Не указано"}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Recommendations;
