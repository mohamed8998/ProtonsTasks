import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';   // Import css file from Bootstrap
import Home from './Components/Home';             //Importing the components for different pages
import Apples from './Components/Apples';          // 
import Bananas from './Components/Bananas';         //
import Oranges from './Components/Orange';           //
import Strawberries from './Components/Strawberries'; //

function App() {
  return (
    <Router>         {/* The app in a Router to enable routing between pages*/}
      <Routes>        {/* Defining the different paths of the app */}
        <Route path="/" element={<Home />} />   {/* Each Route component connects a URL path to a specific component to be displayed*/}
        <Route path="/apples" element={<Apples />} /> 
        <Route path="/bananas" element={<Bananas />} />
        <Route path="/oranges" element={<Oranges />} />
        <Route path="/strawberries" element={<Strawberries />} />
      </Routes>
    </Router>
  );
}

export default App;

