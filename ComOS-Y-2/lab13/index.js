const express = require('express');
const app = express();
const port = 3000;

app.set('view engine', 'ejs');

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.get('/dynamic', (req,res) => {
  const name = req.query.name || 'Guest';
  res.render('dynamic', {name: name});
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});

