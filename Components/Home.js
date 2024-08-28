import React from 'react';
import { Link } from 'react-router-dom';
import { Button, Container } from 'react-bootstrap';

function Home() {
  return (
    <Container>
      <h1>Fruit Counter App</h1>
      <Link to="/apples"><Button variant="primary">Apples</Button></Link>
      <Link to="/bananas"><Button variant="warning">Bananas</Button></Link>
      <Link to="/oranges"><Button variant="danger">Oranges</Button></Link>
      <Link to="/strawberries"><Button variant="success">Strawberries</Button></Link>
    </Container>
  );
}

export default Home;
