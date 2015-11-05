var React = require('react');

var EntryTitle = React.createClass({
  render : function(){
    return (
      <div className='entries-title'>{this.props.text}</div>
    )
  }
});

module.exports = EntryTitle;
