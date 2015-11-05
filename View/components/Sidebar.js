var React = require('react');
var Title = require('./Title');

var Sidebar = React.createClass({
  render : function () {
    return <div className='titles'>
        {this.props.data.map(function(title){
          console.log(this.props.count[title.fields.title_text]);
          return (
            <Title
              text={title.fields.title_text}
              id={title.pk}
              key={title.pk}
              count={this.props.count[title.fields.title_text]}>
              </Title>
          )
        }.bind(this)
      )}
      </div>
    }
});


module.exports = Sidebar
