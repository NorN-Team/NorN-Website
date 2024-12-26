import React from "react";
import { Link } from "react-router-dom";
import "./SearchResults.css";

const SearchResults = ({ results, userId }) => (
  <div className="search-results-container">
    <h3 className="search-results-title">Результаты поиска</h3>
    <div className="search-results-list">
      {results.length > 0 ? (
        results.map((movie) => (
          <div className="search-results-item" key={movie.id}>
            <div className="search-results-poster">Постер</div>
            <div className="search-results-item-content">
              <h4 className="search-results-item-title">
                <Link 
                  to={`/movies/${movie.id}`}
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

export default SearchResults;