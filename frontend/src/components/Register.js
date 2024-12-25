import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./LoginRegister.css";

const Register = () => {
  const navigate = useNavigate();
  const [showPassword, setShowPassword] = useState(false);

  const handleRegister = () => {
    // Здесь вы можете добавить логику регистрации
    navigate("/main"); // Перенаправление на главную страницу после регистрации
  };

  const togglePasswordVisibility = () => {
    setShowPassword((prevState) => !prevState); // Переключаем состояние
  };

  const handleLoginClick = () => {
    navigate("/login"); // Переход на страницу входа
  };

  return (
    <div className="login-register-container">
      <div className="login-register-box">
        <h2>Регистрация</h2>
        <form onSubmit={(e) => e.preventDefault()}>
          <input type="text" placeholder="Имя" />
          <input type="email" placeholder="Email" />
          <div className="password-container">
            <input
              type={showPassword ? "text" : "password"}
              placeholder="Пароль"
            />
            <button
              type="button"
              className="toggle-password"
              onClick={togglePasswordVisibility}
            >
              {showPassword ? "Скрыть пароль" : "Показать пароль"}
            </button>
          </div>
          <button type="submit" onClick={handleRegister}>
            Зарегистрироваться
          </button>
        </form>
        <div className="redirect-link" onClick={handleLoginClick}>
          Уже есть аккаунт? Войдите
        </div>
      </div>
    </div>
  );
};

export default Register;
