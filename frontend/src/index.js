import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

// Найдите корневой элемент
const rootElement = document.getElementById('root');

// Создайте корень и отрендерите приложение
const root = ReactDOM.createRoot(rootElement);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);