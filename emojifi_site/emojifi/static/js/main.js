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
  var queryType = $('#typeselector').val();
  $.ajax({
		method: "POST",
		url: "/emojifi",
		dataType: 'json',
		data: JSON.stringify({
      text: textToSend,
      type: queryType,
    })
	}).done(updateResponseField)
}

function addTypeSelectOptions(response){
  for (let type of response['types']){
    $('#typeselector').append($("<option></option>")
                    .attr("value",type)
                    .text(type));
  }
}
$('#maintextbox').on('input',function(e){
    sendText();
});
$.ajax({
  method: "GET",
  url: "/emojifi_types",
  data: "",
}).done(addTypeSelectOptions)
