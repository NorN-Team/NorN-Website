import React, { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import './AddMovie.css';

const AddMovie = () => {
  const location = useLocation(); // Получаем location для доступа к state
  const { userId } = location.state || {}; // Извлекаем userId из state
  const [title, setTitle] = useState('');
  const [year, setYear] = useState('');
  const [genres, setGenres] = useState('');
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  const handleAddMovie = async (e) => {
    e.preventDefault();
  
    const movieData = {
      title: title.trim(),
      year: parseInt(year, 10),
      genres: genres.split(',').map((genre) => genre.trim()), // Преобразуем в массив строк
    };
  
    try {
      const response = await fetch('http://127.0.0.1:8000/add-movie', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(movieData),
      });
  
      if (response.ok) {
        setMessage('Фильм успешно добавлен!');
        setTitle('');
        setYear('');
        setGenres('');
      } else {
        const errorData = await response.json();
        setMessage(`Ошибка: ${errorData.detail}`);
      }
    } catch (error) {
      setMessage(`Ошибка сервера: ${error.message}`);
    }
  };
  

  const handleBack = () => {
    navigate("/main", { state: { userId } });
  };

  return (
    <div className="add-movie-container">
      <button className="back-button" onClick={handleBack}>
        Назад
      </button>
      <h2 className="add-movie-header">Добавить фильм</h2>
      <form className="add-movie-form" onSubmit={handleAddMovie}>
        <div>
          <label htmlFor="title">Название фильма:</label>
          <input
            id="title"
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="year">Год выпуска:</label>
          <input
            id="year"
            type="number"
            value={year}
            onChange={(e) => setYear(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="genres">Жанры (через запятую):</label>
          <input
            id="genres"
            type="text"
            value={genres}
            onChange={(e) => setGenres(e.target.value)}
            required
          />
        </div>
        <button className="add-movie-button" type="submit">
          Добавить фильм
        </button>
      </form>
      {message && <p className="success-message">{message}</p>}
    </div>
  );
};

export default AddMovie;
