var React = require('react');
var ajax = require('jquery').ajax;
var Title = require('./Title');
var Entry = require('./Entry');
var EntryTitle = require('./EntryTitle');

var Content = React.createClass({
  getInitialState: function(){
    return {
      currentTitle : [],
      currentTitleText : [],
    };
  },
  componentWillMount: function(){
    this.fetchEntries(this.props.params.titleId)
  },
  componentWillReceiveProps: function(nextProps){
    this.fetchEntries(nextProps.params.titleId);
  },
  fetchEntries: function(titleId) {
    ajax({
      dataType:"json",
      url:"http://127.0.0.1:8000/title/"+titleId,
      success: function(data){
        this.setState({
          currentTitle:data.entries,
          currentTitleText:data,
        });
      }.bind(this),
    })
  },
  render : function(){
    // console.log(this.state.currentTitleText.title_text);
    return (

      <div className='entries' >
      {console.log(this.state.currentTitleText)}
      {console.log(this.state.currentTitle)}

      <EntryTitle  text={this.state.currentTitleText.title_text} key={this.state.currentTitleText.id} />

      {this.state.currentTitle.map(function(entry){
        return <Entry text={entry.entry_text} key={entry.id}/>
      })}
      </div>
    );
  }
});


module.exports = Content;
