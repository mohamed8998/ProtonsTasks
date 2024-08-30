import React, { useState } from 'react';
import { Container, Button, Form } from 'react-bootstrap';

function Orange() {
  const [count, setCount] = useState(0);   //count  القيمة الحالية // set count لتحديث القيمة

  return (
    <Container>
      <h1>Orange</h1>
      <p>Count: {count}</p>  {/* Display the current number of orange*/}
      <Button variant="danger" onClick={() => setCount(count + 1)}>Add</Button>  {/* Add a button to increase a number and variable allow you to define the styles can used colors */}
      <Button variant="secondary" onClick={() => setCount(count - 1)}>-</Button> {/* Add a button to decrease a number and variable allow you to define the styles can used colors */}
      <Form.Control  // Enter a specific number
        type="number"  // Input type as number
        value={count}   // Bind a value to a state count
        onChange={(e) => setCount(Number(e.target.value))}  // Update count status with the new value
        style={{ width: '100px', marginTop: '10px' }}   // styling the width and marigin top
      />
    </Container>
  );
}

export default Orange;
