import React, { useState } from 'react';
import { Container, Button, Form } from 'react-bootstrap';

function Orange() {
  const [count, setCount] = useState(0);

  return (
    <Container>
      <h1>Orange</h1>
      <p>Count: {count}</p>
      <Button variant="danger" onClick={() => setCount(count + 1)}>Add</Button>
      <Button variant="secondary" onClick={() => setCount(count - 1)}>-</Button>
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
