var React = require('react');
var ReactDOM = require('react-dom');
var Router = require('react-router').Router;
var Route = require('react-router').Route;
var Hello = require('./Hello');
var Content = require('./components/Content');

var Routes=(
  <Router>
    <Route path="/" component={ Hello }>
      <Route path="title/:titleId" component={ Content } />
    </Route>
  </Router>
);

ReactDOM.render(Routes, document.getElementById('content'))
