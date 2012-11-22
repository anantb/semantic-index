<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
<title>Parser</title>
</head>
<body>
	<h1>Parser</h1>
	<hr />
	Please enter the sentence below: <br />
    <textarea id="input-text" rows="4" cols="50"></textarea>
	<br />
	<input type="button" id="parse" value="Submit" />
	<br />
	</form>
	<br />
	<div id= "output">
	</div>
	<script type="text/javascript">
	$("#parse").click(function(){
	    $("#output").html("Loading...")
	    $("#output").load('parser.jsp?input='+encodeURIComponent($("#input-text").val()));
		
	});
   </script>
</body>
</html>