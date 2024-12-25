import React, { useState } from "react";
import Slider from "rc-slider";
import "./Filters.css";
import "rc-slider/assets/index.css"; // Импорт стилей для rc-slider

const Filters = ({ setMovies }) => {
  const [titleSubstring, setTitleSubstring] = useState(""); // Подстрока для поиска
  const [genres, setGenres] = useState([]); // Жанры
  const [yearRange, setYearRange] = useState([1980, 2024]); // Диапазон годов

  // Функция для выполнения поиска на сервере
  const handleSearch = async () => {
    try {
      const params = new URLSearchParams();

      if (titleSubstring) params.append("title_substr", titleSubstring);
      if (genres.length > 0) {
        genres.forEach((genre) => params.append("genres", genre));
      }
      if (yearRange[0] !== undefined) params.append("start_year", yearRange[0]);
      if (yearRange[1] !== undefined) params.append("end_year", yearRange[1]);

      console.log(`Запрос: http://127.0.0.1:8000/movies/filter?${params.toString()}`);

      const response = await fetch(`http://127.0.0.1:8000/movies/filter?${params.toString()}`);
      if (!response.ok) {
        throw new Error("Ошибка запроса к API");
      }

      const data = await response.json();
      setMovies(data); // Сохраняем фильмы в родительском состоянии
    } catch (error) {
      console.error("Ошибка:", error);
    }
  };

  return (
    <div className="filters-container">
      <h3>Фильтрация фильмов</h3>

      {/* Поле для ввода подстроки */}
      <div className="filter-title">
        <label>
          Название (подстрока):
          <input
            type="text"
            value={titleSubstring}
            onChange={(e) => setTitleSubstring(e.target.value)}
          />
        </label>
      </div>

      {/* Ползунок для выбора диапазона лет */}
      <div className="filter-year">
        <label>Диапазон лет: {yearRange[0]} - {yearRange[1]}</label>
        <Slider
          range
          allowCross={false}
          min={1980}
          max={2024}
          defaultValue={yearRange}
          onChange={(value) => setYearRange(value)} // Обновляем диапазон
          trackStyle={[{ backgroundColor: "#4caf50" }]}
          handleStyle={[
            { borderColor: "#4caf50", backgroundColor: "#4caf50" },
            { borderColor: "#4caf50", backgroundColor: "#4caf50" },
          ]}
        />
      </div>

      {/* Поля для выбора жанров (чекбоксы) */}
      <div className="filter-genres">
        <label>Жанры:</label>
        {["Adventure", "Animation", "Children", "Comedy", "Action", "Fantasy", "Thriller", "Sci-Fi", "Crime", "Drama", "Romance"].map((genre) => (
          <div key={genre} className="genre-checkbox">
            <input
              type="checkbox"
              value={genre}
              onChange={(e) => {
                if (e.target.checked) {
                  setGenres([...genres, genre]);
                } else {
                  setGenres(genres.filter((g) => g !== genre));
                }
              }}
              className="checkbox"
            />
            {genre}
          </div>
        ))}
      </div>

      <button className="search-button" onClick={handleSearch}>
        Поиск
      </button>
    </div>
  );
};

export default Filters;
