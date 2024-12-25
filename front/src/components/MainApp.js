import React, { useState } from "react";
import "./MainApp.css";
import Header from "./Header";
import Filters from "./Filters";
import SearchResults from "./SearchResults";
import Recommendations from "./Recommendations";

const App = () => {
  const [movies, setMovies] = useState([]); // Состояние для хранения результатов поиска

  return (
    <div className="app-container"> {/* Класс для общего контейнера */}
      <header className="header"> {/* Класс для шапки */}
        <Header />
      </header>

      <div className="main-content"> {/* Класс для основного содержимого */}
        <div className="sidebar-left"> {/* Класс для левой колонки */}
          {/* Передаем setMovies в Filters */}
          <Filters setMovies={setMovies} />
        </div>
        <div className="results"> {/* Класс для центральной колонки */}
          {/* Передаем результаты поиска в SearchResults */}
          <SearchResults results={movies} />
        </div>
        <div className="sidebar-right"> {/* Класс для правой колонки */}
          <Recommendations />
        </div>
      </div>

      <footer className="footer"> {/* Класс для футера */}
        © 2024 Онлайн-кинотеатр
      </footer>
    </div>
  );
};

export default App;
