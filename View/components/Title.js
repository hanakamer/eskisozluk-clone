var React = require('react');
var Link = require('react-router').Link;

var Title = React.createClass({
  render : function (){
    return (
      <div>
        <div className='entry-title'>
          <Link to={'/title/'+this.props.id}>{this.props.text}</Link>
          <span className='num-of-entry'>{this.props.count}</span>
        </div>
        <hr />
      </div>
    )
  }
});

module.exports = Title;
