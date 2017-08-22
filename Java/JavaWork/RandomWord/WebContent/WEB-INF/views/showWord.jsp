<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Random Word Generator</title>
</head>
<body>
	<h3>You have generated a word <%= session.getAttribute("click") %> times</h3>
	<p><%= session.getAttribute("word") %></p>
	<form action="word" method="post">
  		<input type="submit" value="Generate">
	</form>
	<h3>The last time you generated a word was:</h3>
	<p><%= session.getAttribute("time") %></p>
</body>
</html>