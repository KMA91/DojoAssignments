package com.kevinma.pet.controllers;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
//import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.kevinma.pet.models.Dog;

public class getDog extends HttpServlet {
	private static final long serialVersionUID = 1L;
 
 
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Process Request:
        String name = request.getParameter("name");
        String breed = request.getParameter("breed");
        int weight = Integer.parseInt(request.getParameter("weight"));
        // Create model
        Dog dog = new Dog(name, breed, weight);
        // Set Model for view
        request.setAttribute("dog", dog);
        // Let view handle the request
        RequestDispatcher view = request.getRequestDispatcher("/WEB-INF/views/showDog.jsp");
        view.forward(request, response);
	}

	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
//        String name = request.getParameter("name");
//        String breed = request.getParameter("breed");
//        int weight = Integer.parseInt(request.getParameter("weight"));
	}

}
