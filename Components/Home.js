import React from 'react';
import { Link } from 'react-router-dom';   // It is used to create links to navigate between different pages 
import { Button, Container } from 'react-bootstrap';

function Home() {
  return (
    <Container>  {/* It is used to wrap content and to provide space */}
      <h1>Fruit App</h1>
      <Link to="/apples"><Button variant="primary">Apples</Button></Link>    
      <Link to="/bananas"><Button variant="warning">Bananas</Button></Link>
      <Link to="/oranges"><Button variant="danger">Oranges</Button></Link>
      <Link to="/strawberries"><Button variant="success">Strawberries</Button></Link>
    </Container>
  );
}

export default Home;
