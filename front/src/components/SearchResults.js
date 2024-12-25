import React from 'react';

const SearchResults = () => (
  <div style={{ padding: '10px' }}>
    <h3>Результаты поиска</h3>
    <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
      {/* Замена данных на статичные */}
      {[1, 2, 3].map((_, idx) => (
        <div key={idx} style={{ display: 'flex', alignItems: 'center', gap: '10px', marginTop: '20px' }}>
          <div style={{ width: '75px', height: '105px', background: 'white' }}></div>
          <div>
            <h4>Название фильма {idx + 1}</h4>
            <p>Жанр: Комедия</p>
          </div>
        </div>
      ))}
    </div>
  </div>
);

export default SearchResults;