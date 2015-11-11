var React = require('react');
var Title = require('./Title');

var Sidebar = React.createClass({
  render : function () {
    return <div className='titles'>
        {this.props.data.map(function(title){
          return (
            <Title
              text={title.title_text}
              id={title.id}
              key={title.id}
              count={title.entries__count}>
              </Title>
          )
        }.bind(this)
      )}
      </div>
    }
});


module.exports = Sidebar
