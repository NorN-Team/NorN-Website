import React, { useState } from "react";
import { useLocation } from "react-router-dom"; // Импорт для получения данных из state
import "./MainApp.css";
import Header from "./Header";
import Filters from "./Filters";
import SearchResults from "./SearchResults";
import Recommendations from "./Recommendations";

const App = () => {
  const location = useLocation();
  const { userId } = location.state || {}; // Получаем user_id из state, если он передан
  const [movies, setMovies] = useState([]); // Состояние для хранения результатов поиска

  return (
    <div className="app-container"> {/* Класс для общего контейнера */}
      <header className="header"> {/* Класс для шапки */}
        <Header /> {/* Передаем userId в Header */}
      </header>

      <div className="main-content"> {/* Класс для основного содержимого */}
        <div className="sidebar-left"> {/* Класс для левой колонки */}
          {/* Передаем setMovies и userId в Filters */}
          <Filters setMovies={setMovies} />
        </div>
        <div className="results"> {/* Класс для центральной колонки */}
          {/* Передаем результаты поиска в SearchResults */}
          <SearchResults results={movies} userId={userId}/>
        </div>
        <div className="sidebar-right"> {/* Класс для правой колонки */}
          <Recommendations userId={userId} /> {/* Передаем userId в Recommendations */}
        </div>
      </div>

      <footer className="footer"> {/* Класс для футера */}
        © 2024 Онлайн-кинотеатр
      </footer>
    </div>
  );
};

export default App;
