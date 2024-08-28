import React, { useState } from 'react';
import { Container, Button, Form } from 'react-bootstrap';

function Orange() {
  const [count, setCount] = useState(0);

  return (
    <Container>
      <h1>Bananas</h1>
      <p>Count: {count}</p>
      <Button variant="warning" onClick={() => setCount(count + 1)}>Increment</Button>
      <Button variant="secondary" onClick={() => setCount(count - 1)}>Decrement</Button>
      <Form.Control
        type="number"
        value={count}
        onChange={(e) => setCount(Number(e.target.value))}
        style={{ width: '100px', marginTop: '10px' }}
      />
    </Container>
  );
}

export default Orange;
