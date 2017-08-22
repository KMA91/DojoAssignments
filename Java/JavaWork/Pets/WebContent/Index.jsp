<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
    
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Pets</title>
</head>
<body>
	<h3>Make a Dog!</h3>
	<form action="dog" method="POST">
		Name: <input type="text" name="name">
		Breed: <input type="text" name="breed">
		Weight(lbs): <input type="text" name="weight">
		<input type="submit" name="Submit">
	</form>
	
	<h3>Make a Cat!</h3>
	<form action="/cat" method="POST">
		Name: <input type="text" name="name">
		Breed: <input type="text" name="breed">
		Weight(lbs): <input type="text" name="weight">
		<input type="submit" name="Submit">
	</form>

</body>
</html>