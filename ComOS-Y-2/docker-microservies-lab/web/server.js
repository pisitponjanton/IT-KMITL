const express = require('express');
const mongoose = require('mongoose');

const app = express();
app.use(express.urlencoded({ extended: true }));

app.set('view engine', 'ejs');
app.set('views', './views');

mongoose.connect('mongodb://mongo:27017/students');

const Student = mongoose.model('Student', {
  firstName: String,
  lastName: String,
  studentId: String
});

app.get('/', async (req, res) => {
  const students = await Student.find();
  res.render('index', { students });
});

app.post('/add', async (req, res) => {
  await Student.create(req.body);
  res.redirect('/');
});

app.listen(3000, () => {
  console.log('Web service running on port 3000');
});
