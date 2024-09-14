import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import Home from './Components/Home';          // Fix the file name
import Apples from './Components/Apples';      // Fix the file name
import Bananas from './Components/Bananas';     // Fix the file name, remove space
import Oranges from './Components/Orange';    // Fix the file name
import Strawberries from './Components/Strawberries';  // Fix the file name, remove space

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
