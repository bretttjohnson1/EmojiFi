var currentEndpoint = "/clapifi"

function updateResponseField(response){
  $("#response_field").text(response.text)
}
function sendText(){
  var textToSend = $("#maintextbox").val();
  $.ajax({
		method: "POST",
		url: currentEndpoint,
		dataType: 'json',
		data: JSON.stringify({ text: textToSend })
	}).done(updateResponseField)
}

$('#maintextform').submit(function () {
 //e.preventDefault();
  sendText();
  return false;
});
