import React from 'react';
import logo from '../images/logo.jpg'; // Путь к изображению

const Header = () => (
  <header style={{ display: 'flex', alignItems: 'center', padding: '10px', background: '#4caf50', color: '#d4edda', borderRadius: '8px', justifyContent: 'space-between' }}>
    <div style={{ display: 'flex', alignItems: 'center' }}>
      <img
        src={logo}
        alt="Логотип"
        style={{
          width: '100px',
          height: 'auto',
          marginRight: '10px',
          borderRadius: '8px', // Скругление углов
        }}
      />
    </div>
  </header>
);

export default Header;