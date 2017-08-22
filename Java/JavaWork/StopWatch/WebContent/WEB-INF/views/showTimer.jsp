<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
<p> 
<form action="start" method="post">
  		<button>Start</button>
</form> 
<form action="stop" method="post">
  		<button>Stop</button>
</form> 
	<form action="reset" method="post">
  		<button>Reset</button>
</form> 
<p> 
Start: 
<% if(session.getAttribute("start_time") != null){ %>
<%= session.getAttribute("start_time") %>
<% } %> 
Current time: <%= session.getAttribute("current_time") %> 
Running Time: 
<% if(session.getAttribute("start_time") != null){%>
<%= session.getAttribute("running_ms") %>
<% } %>
</p>
<table>
  <tr>
    <th>Start</th>
    <th>Stop</th>
    <th>Reset</th>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>
</body>
</html>