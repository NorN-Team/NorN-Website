import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./LoginRegister.css";

const Login = () => {
  const navigate = useNavigate();
  const [showPassword, setShowPassword] = useState(false); // Состояние для показа/скрытия пароля

  const togglePasswordVisibility = () => {
    setShowPassword((prevState) => !prevState); // Переключаем состояние
  };

  const handleLogin = () => {
    navigate("/main"); // Перенаправление на главную страницу после входа
  };

  const handleRegisterClick = () => {
    navigate("/register"); // Переход на страницу регистрации
  };

  return (
    <div className="login-register-container">
      <div className="login-register-box">
        <h2>Вход</h2>
        <form onSubmit={(e) => e.preventDefault()}>
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
          <button type="submit" onClick={handleLogin}>
            Войти
          </button>
        </form>
        <div className="redirect-link" onClick={handleRegisterClick}>
          Нет аккаунта? Зарегистрируйтесь
        </div>
      </div>
    </div>
  );
};

export default Login;
