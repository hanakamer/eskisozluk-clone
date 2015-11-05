var React = require('react');
var ajax = require('jquery').ajax;

var EntryForm = React.createClass({
  handleSubmit: function(e){
    e.preventDefault();
    var title = this.refs.title.value.trim();
    var entry =  this.refs.entry.value.trim();
    if (!title || !entry) {
      return;
    }
    var data = {
      title: title,
      entry : entry,
    }
    // SEND REQUEST TO SERVER!!!!!!s
    ajax({
      type: 'POST',
      url: "http://127.0.0.1:8000/submit_entry/",
      data:data,
      success: function(data){
        window.location="http://localhost:8080/#/title/"+data.id;
      }
    })

    this.refs.title.value = '';
    this.refs.entry.value = '';
    return;
  },
  render :function(){
    return (
    <div>
        <form className="input-area" onSubmit={this.handleSubmit}>
          <input placeholder="baslik, #entry ya da @yazar" ref='title' />
          <textarea className="entry-textarea" cols="50" rows="3" placeholder="entry icerigi" ref='entry' />
          <input type='submit' value='post' className='send-button'/>
        </form>
    </div>
  )}
});
module.exports = EntryForm
