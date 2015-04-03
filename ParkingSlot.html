<!DOCTYPE html>
<html>
	<head><meta charset="UTF-8">
		<title>Title of the document</title>
	</head>
	<style>
	div{
		color: Yellow;
		background: Blue;
		font-family: "Arial";
		font-size: 50px;
		width: 200px;
		height: 200px;

	}
	</style>

	<body>
		<div id="slot1" style="position:relative; float:left  ">
			Slot 1
		</div>
		<div id="slot2" style="position:relative; float:left  ">
			Slot 2
		</div>
		<div id="slot3" style="position:relative; float:left  ">
			Slot 3
		</div>
		<div id="slot4" style="position:relative; float:left  ">
			Slot 4
		</div>

		<input type="button" name="updateButton" value="Instant Update!"onClick="sendingRequest();">

	</body>
	<script language="javascript" type="text/javascript" >
	var socket = new WebSocket("ws://localhost:8000/");
	var automatic = false;
	var interval = 3000;
	
	socket.onmessage = function(event){
		updateContent(event.data);
	}
	function sendingRequest(){
		socket.send("update");
	}
	function updateContent(string){
		var slots = string.split(",");
		for (i = 0; i < slots.length;i++){
			var content = slots[i].split(":");
			var dom = document.querySelector("#"+content[0]);
			if (content[1] == "True"){
				console.log(content[0] + " is busy");
				dom.style.background = "Red";
			} else {
				console.log(content[0] + " is avalable");
				dom.style.background = "Green";
			}
		}
	}
	window.setInterval(sendingRequest, interval);
	
	</script>
</html>
