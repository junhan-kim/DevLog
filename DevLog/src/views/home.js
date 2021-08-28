import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Home = (props) => {
  useEffect(() => {
    axios
      .post('http://localhost:5000/auth/login', {
        email: 'famousss@gmail.com',
        password: '1234',
      })
      .then((res) => setState(res.data.Authorization));
  }, []);

  const [state, setState] = useState('');

  return (
    <div>
      Home
      <p>{state}</p>
    </div>
  );
};

export default Home;
