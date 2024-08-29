import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import Home from './Components/Home';   
import Apples from './Components/Apples';
import Bananas from './Components/Bananas';
import Oranges from './Components/Orange';
import Strawberries from './Components/Strawberries';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/apples" element={<Apples />} />
        <Route path="/bananas" element={<Bananas />} />
        <Route path="/oranges" element={<Oranges />} />
        <Route path="/strawberries" element={<Strawberries />} />
      </Routes>
    </Router>
  );
}

export default App;
