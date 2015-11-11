var React = require('react');
var ajax = require('jquery').ajax;
var EntryForm = require('./components/EntryForm');
var Sidebar = require('./components/Sidebar');
var Content = require('./components/Content');


// http://localhost:3000/api/titles
// http://localhost:3000/api/entries?title=1

// function testAjax(){
//   return $.ajax({
//     async: false,
//     url: "http://127.0.0.1:8000/titles/",
//     success:function(data) {
//         var result = data;
//       }
//   });
//   return result;
// }
// var promise = testAjax();
// var data = promise.responseText
// console.log(data)
// console.log(JSON.parse(data))
// data = JSON.parse(data)


module.exports =  React.createClass({
  displayName:'Hello',
  getInitialState: function(){
    return {
      titles : [],
      entryNum:[],
    };
  },
  componentWillMount: function(){
    ajax({
      dataType:"json",
      url: "http://127.0.0.1:8000/titles/",
      success: function(data){
        this.setState({
          titles:data,
          entryNum:data,
        });
      }.bind(this),
    })
  },
  render : function(){
    return (
      <div>
      <EntryForm />
        <Sidebar data={this.state.titles} count={this.state.entryNum} />
        {this.props.children}
      </div>
  )}
});
