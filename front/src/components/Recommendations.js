import React from 'react';

const Recommendations = () => (
  <div style={{ padding: '10px', borderLeft: '1px solid #ddd' }}>
    <h3>Рекомендации</h3>
    {[1, 2].map((_, idx) => (
      <div key={idx} style={{ display: 'flex', alignItems: 'center', gap: '10px', marginTop: '15px', marginBottom: '10px' }}>
        <div style={{ width: '75px', height: '105px', background: 'white' }}></div>
        <div>
          <h4>Рекомендованный фильм {idx + 1}</h4>
          <p>Жанр: Драма</p>
        </div>
      </div>
    ))}
  </div>
);

export default Recommendations;