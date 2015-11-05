var React = require('react');

var Entry = React.createClass({
  render : function(){
    return (
      <div>
        <div className='entry'>{this.props.text}</div>
        <hr />
      </div>
    )
  }
});

module.exports = Entry;
