package com.stopwatch.controllers;

import java.io.IOException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.concurrent.TimeUnit;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
//import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;


public class Start extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		HttpSession session = request.getSession();
		LocalDateTime now = LocalDateTime.now();
		DateTimeFormatter formatter = DateTimeFormatter.ofPattern("h:mm a");
		String timeformat = now.format(formatter);
		session.setAttribute("current_time", timeformat);
		if(session.getAttribute("start_time") != null){
			long startTime = (long) session.getAttribute("ms_start");
			long endTime = (long) System.currentTimeMillis();
			long totalTime = endTime - startTime;
			String newtotalTime = String.format("%d min, %d sec", 
				    TimeUnit.MILLISECONDS.toMinutes(totalTime),
				    TimeUnit.MILLISECONDS.toSeconds(totalTime) - 
				    TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes(totalTime))
				);
			session.setAttribute("running_ms", newtotalTime);
		}
		RequestDispatcher view = request.getRequestDispatcher("/WEB-INF/views/showTimer.jsp");
        view.forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		HttpSession session = request.getSession();
		LocalDateTime now = LocalDateTime.now();
		DateTimeFormatter formatter = DateTimeFormatter.ofPattern("h:mm a");
		String timeformat = now.format(formatter);
		session.setAttribute("start_time", timeformat);
		session.setAttribute("ms_start", System.currentTimeMillis());
		doGet(request, response);
	}

}