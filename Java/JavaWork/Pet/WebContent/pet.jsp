<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Make a pet!</title>
</head>
<body>
<h4>Make a Dog</h4>
	<form action="dog" method="post">
  		<input type="text" name="name" placeholder="Name">
  		<input type="text" name="breed" placeholder="Breed">
  		<input type="number" name="weight" placeholder="Weight">
  		<input type="submit" value="submit">
	</form>

<h4>Make a Cat</h4>
	<form action="cat" method="post">
  		<input type="text" name="name" placeholder="Name">
  		<input type="text" name="breed" placeholder="Breed">
  		<input type="number" name="weight" placeholder="Weight">
  		<input type="submit" value="submit">
	</form>
</body>
</html>