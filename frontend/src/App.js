import React from "react";
import { Routes, Route } from "react-router-dom";
import Login from "./components/Login";
import MoviePage from "./components/MoviePage";
import Register from "./components/Register";
import MainApp from "./components/MainApp";
import AddMoviePage from './components/AddMovie'; 

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/login" element={<Login />} />
      <Route path="/movies/:id" element={<MoviePage />} />
      <Route path="/register" element={<Register />} />
      <Route path="/main" element={<MainApp />} />
      <Route path="/add-movie" element={<AddMoviePage />} />
    </Routes>
  );
};

export default App;
