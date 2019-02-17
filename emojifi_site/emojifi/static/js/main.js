var last_post_time = 0;
var scheduled = false;

function updateResponseField(response){
  $("#textresult").text(response.text)
  if (response.text == ""){
    $("#textresult").css("padding", "0px")
  }else{
    $("#textresult").css("padding", "20px")
  }
}
function sendText(){
  last_post_time = (new Date()).getTime();
  var textToSend = $("#maintextbox").val();
  var queryType = $('#typeselector').val();
  scheduled = false;
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
    if (!scheduled){
      scheduled = true;
      setTimeout(sendText, 500);
    }
});
$('#typeselector').on('change', function() {
   sendText();
 });
$.ajax({
  method: "GET",
  url: "/emojifi_types",
  data: "",
}).done(addTypeSelectOptions)
