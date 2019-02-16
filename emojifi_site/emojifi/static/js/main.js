var currentEndpoint = "/clapifi"

function updateResponseField(response){
  $("#textresult").text(response.text)
  if (response.text == ""){
    $("#textresult").css("padding", "0px")
  }else{
    $("#textresult").css("padding", "20px")
  }
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

$('#maintextbox').on('input',function(e){
    sendText();
});
