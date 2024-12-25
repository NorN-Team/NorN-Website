import React from "react";

const SearchResults = ({ results }) => (
  <div style={{ padding: "10px" }}>
    <h3>Результаты поиска</h3>
    <div style={{ display: "flex", flexDirection: "column", gap: "10px" }}>
      {results.length > 0 ? (
        results.map((movie, idx) => (
          <div
            key={idx}
            style={{
              display: "flex",
              alignItems: "flex-start",
              gap: "20px",
              marginTop: "20px",
            }}
          >
            <div
              style={{
                width: "75px",
                height: "105px",
                background: "white",
                flexShrink: 0, // Фиксируем размер картинки
              }}
            ></div>
            <div
              style={{
                display: "flex",
                flexDirection: "column",
                alignItems: "flex-start", // Выравнивание по левому краю
              }}
            >
              <h4 style={{ margin: 0 }}>{movie.title}</h4>
              <p style={{ marginTop: 10 }}>Жанры: {movie.genres.join(", ")}</p>
            </div>
          </div>
        ))
      ) : (
        <p>Нет фильмов, соответствующих критериям.</p>
      )}
    </div>
  </div>
);

export default SearchResults;
