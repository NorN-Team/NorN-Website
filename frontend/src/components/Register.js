import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./LoginRegister.css";

const Register = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [usernameError, setUsernameError] = useState("");
  const [passwordError, setPasswordError] = useState("");

  const handleRegister = async () => {
    // Проверка данных перед отправкой
    if (!validateFields()) return;

    try {
      const response = await fetch("http://localhost:8000/auth/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        navigate("/login"); // Перенаправление на главную страницу после регистрации
      } else {
        const errorData = await response.json();
        alert(errorData.detail || "Ошибка регистрации");
      }
    } catch (error) {
      alert("Не удалось подключиться к серверу");
    }
  };

  const validateFields = () => {
    let isValid = true;

    // Проверка имени пользователя
    if (username.length < 1) {
      setUsernameError("Имя пользователя должно содержать хотя бы 1 символ.");
      isValid = false;
    } else {
      setUsernameError(""); // Сброс ошибки
    }

    // Проверка пароля
    if (password.length < 8) {
      setPasswordError("Пароль должен содержать не менее 8 символов.");
      isValid = false;
    } else {
      setPasswordError(""); // Сброс ошибки
    }

    return isValid;
  };

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
    if (e.target.value.length >= 1) {
      setUsernameError(""); // Убираем ошибку при вводе валидного имени
    }
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
    if (e.target.value.length >= 8) {
      setPasswordError(""); // Убираем ошибку при вводе валидного пароля
    }
  };

  const togglePasswordVisibility = () => {
    setShowPassword((prevState) => !prevState);
  };

  const [showPassword, setShowPassword] = useState(false);

  return (
    <div className="login-register-container">
      <div className="login-register-box">
        <h2>Регистрация</h2>
        <form onSubmit={(e) => e.preventDefault()}>
            <input
              type="text"
              placeholder="Имя"
              value={username}
              onChange={handleUsernameChange}
              className={usernameError ? "input-error" : ""}
            />
            {usernameError && <div className="error-message">{usernameError}</div>}
          <div className="password-container">
            <input
              type={showPassword ? "text" : "password"}
              placeholder="Пароль"
              value={password}
              onChange={handlePasswordChange}
              className={passwordError ? "input-error" : ""}
            />
            <button
              type="button"
              className="toggle-password"
              onClick={togglePasswordVisibility}
            >
              {showPassword ? "Скрыть пароль" : "Показать пароль"}
            </button>
            {passwordError && <div className="error-message">{passwordError}</div>}
          </div>
          <button type="submit" onClick={handleRegister}>
            Зарегистрироваться
          </button>
        </form>
        <div className="redirect-link" onClick={() => navigate("/login")}>
          Уже есть аккаунт? Войдите
        </div>
      </div>
    </div>
  );
};

export default Register;
