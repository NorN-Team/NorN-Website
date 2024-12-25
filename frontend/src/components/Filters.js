import React, { useState } from 'react';
import './Filters.css';

const Filters = () => {
  // Изначально все фильтры выключены
  const [selectedGenres, setSelectedGenres] = useState([]);

  // Массив жанров
  const genres = ['Драма', 'Комедия', 'Экшн', 'Ужасы'];

  // Функция для обработки изменения состояния чекбокса
  const handleCheckboxChange = (genre) => {
    setSelectedGenres((prevSelectedGenres) => {
      if (prevSelectedGenres.includes(genre)) {
        // Если жанр уже выбран, удаляем его
        return prevSelectedGenres.filter(item => item !== genre);
      } else {
        // Если жанр не выбран, добавляем его
        return [...prevSelectedGenres, genre];
      }
    });
  };

  return (
    <div style={{ padding: '10px', borderRight: '1px solid #ddd' }}>
      <h3>Фильтрация по жанрам</h3>
      <ul style={{ listStyleType: 'none', paddingLeft: '0' }}>
        {genres.map((genre) => (
          <li key={genre} style={{ marginTop: '15px', marginBottom: '15px' }}>
            <label>
              <input
                type="checkbox"
                checked={selectedGenres.includes(genre)}
                onChange={() => handleCheckboxChange(genre)}
              />
              {genre}
            </label>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Filters;