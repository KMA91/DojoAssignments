<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"
    import="com.teamroster.models.Team, java.util.ArrayList"
    %>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Roster</title>
</head>
<body>
<h3>Prototype Roster</h3>
<a href="NewTeam">New Team</a>
<table>
  <tr>
    <th>Team</th>
    <th>Players</th>
    <th>Action</th>
  </tr>
  
  <% 
  if(session.getAttribute("teams") != null){
  	ArrayList<Team> teams = (ArrayList<Team>) session.getAttribute("teams");
  	for(Team team : teams){%>
  		<tr>
    		<td><%= team.getTeam_name()%></td>
    		<td><%= team.getPlayercount()%></td>
   	 		<td>
   	 			<a href="/TeamRoster/NewTeam/" + <%= team.getIndexof(team) %>>Details</a>
				<a href="#">Delete</a>
   	 				
   	 		</td>
  		</tr>
  <% } %>
 <% } %>
</table>
</body>
</html>