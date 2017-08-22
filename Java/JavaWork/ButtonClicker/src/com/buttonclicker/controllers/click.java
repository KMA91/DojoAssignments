package com.buttonclicker.controllers;
import java.io.IOException;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
//@WebServlet(name = "clicks", urlPatterns = { "/clicks" })
public class click extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		RequestDispatcher view = request.getRequestDispatcher("/WEB-INF/views/button.jsp");
		view.forward(request, response);
	}
	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		HttpSession session = request.getSession();
		int click = (int) session.getAttribute("click");
		click ++;
		session.setAttribute("click", click);		
//		RequestDispatcher view = request.getRequestDispatcher("/WEB-INF/views/button.jsp");
//      view.forward(request, response);
		doGet(request, response);
	}

}