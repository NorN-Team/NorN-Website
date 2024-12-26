import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./LoginRegister.css";

const Login = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  const togglePasswordVisibility = () => {
    setShowPassword((prevState) => !prevState);
  };

  const handleLogin = async () => {
    setErrorMessage(""); // Сброс ошибки перед началом запроса

    try {
      const response = await fetch("http://localhost:8000/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username: email, password }),
      });

      if (response.ok) {
        navigate("/main"); // Перенаправление на главную страницу после успешного входа
      } else {
        const errorData = await response.json();
        setErrorMessage(errorData.detail || "Ошибка входа");
      }
    } catch (error) {
      setErrorMessage("Не удалось подключиться к серверу");
    }
  };

  const handleRegisterClick = () => {
    navigate("/register");
  };

  return (
    <div className="login-register-container">
      <div className="login-register-box">
        <h2>Вход</h2>
        <form onSubmit={(e) => e.preventDefault()}>
          <input
            type="text"
            placeholder="Имя пользователя"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <div className="password-container">
            <input
              type={showPassword ? "text" : "password"}
              placeholder="Пароль"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <button
              type="button"
              className="toggle-password"
              onClick={togglePasswordVisibility}
            >
              {showPassword ? "Скрыть пароль" : "Показать пароль"}
            </button>
          </div>
          {errorMessage && <div className="error-message">{errorMessage}</div>}
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
