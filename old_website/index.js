function send(){
  var a = document.getElementById("message").value
  var data = { "message":a};
  var options={
    method:'POST',
    headers:{
      'Content-Type': 'application/json'
    },
    body:JSON.stringify(data)
    };
  fetch('https://telemessage.herokuapp.com',options)
  document.getElementById("message").value=""
}
