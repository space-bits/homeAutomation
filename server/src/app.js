const express = require('express');
const createError = require('http-errors');
const path = require('path');
const cookieParser = require('cookie-parser');
const logger = require('morgan');
require('./config/config');

const indexRouter = require('./routes/index');
const usersRouter = require('./routes/users');
const tempsRouter = require('./routes/temps');
const sensorsRouter = require('./routes/sensors');
const alarmsRouter = require('./routes/alarms');

const app = express();
app.use(logger(process.env.ENV));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/users', usersRouter);
app.use('/temps', tempsRouter);
app.use('/sensors', sensorsRouter);
app.use('/alarm', alarmsRouter);

// catch 404 and forward to error handler
app.use((req, res, next) => {
  next(createError(404));
});

// error handler
app.use((err, req, res) => {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = process.env.ENV === 'dev' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.json({
    message: err.message,
    error: err,
  });
});

module.exports = app;
