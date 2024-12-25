import React from 'react';
import './App.css';
import Header from './components/Header';
import Filters from './components/Filters';
import SearchResults from './components/SearchResults';
import Recommendations from './components/Recommendations';


const App = () => (
  <div className="app-container"> {/* Класс для общего контейнера */}
    <header className="header"> {/* Класс для шапки */}
       <Header />
    </header>

    <div className="main-content"> {/* Класс для основного содержимого */}
      <div className="sidebar-left"> {/* Класс для левой колонки */}
        <Filters />
      </div>
      <div className="results"> {/* Класс для центральной колонки */}
        <SearchResults />
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

export default App;