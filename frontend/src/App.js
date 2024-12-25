import React from "react";
import { Routes, Route } from "react-router-dom";
import Login from "./components/Login";
import Register from "./components/Register";
import MainApp from "./components/MainApp"; // Главная страница после входа

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/main" element={<MainApp />} />
    </Routes>
  );
};

export default App;
