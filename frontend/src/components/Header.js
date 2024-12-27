import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom'; // Для работы с маршрутизацией
import logo from '../images/logo.jpg'; // Путь к изображению
import './Header.css'; // Подключение CSS файла

const Header = ({ userId }) => {
  const [role, setRole] = useState(null);

  useEffect(() => {
    // Функция для получения роли пользователя
    const fetchUserRole = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/user-role?user_id=${userId}`);
        if (!response.ok) {
          throw new Error('Ошибка загрузки роли пользователя');
        }
        const data = await response.json();
        setRole(data.role); // Устанавливаем роль пользователя
      } catch (error) {
        console.error('Ошибка при получении роли пользователя:', error);
      }
    };

    if (userId) {
      fetchUserRole();
    }
  }, [userId]);

  return (
    <header>
      {/* Логотип */}
      <div>
        <img
          src={logo}
          alt="Логотип"
        />
      </div>
      
      {/* Кнопка для администратора */}
      {role === 'admin' && (
        <nav>
          <Link
            to={"/add-movie"}
            className="admin-button"
            state={{ userId }} 
          >
            Добавить фильм
          </Link>
        </nav>
      )}
    </header>
  );
};

export default Header;
