import React from 'react';
import logo from '../images/logo.jpg'; // Путь к изображению

const Header = () => (
  <header>
    <div style={{ display: 'flex', alignItems: 'center' }}>
      <img
        src={logo}
        alt="Логотип"
        style={{
          width: '100px',
          height: 'auto',
          marginLeft: '10px',
          borderRadius: '8px', // Скругление углов
        }}
      />
    </div>
  </header>
);

export default Header;