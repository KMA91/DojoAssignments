package com.kevinma.pet.controllers;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
//import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.kevinma.pet.models.Cat;

public class getCat extends HttpServlet {
	private static final long serialVersionUID = 1L;
 
 
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Process Request:
        String name = request.getParameter("name");
        String breed = request.getParameter("breed");
        int weight = Integer.parseInt(request.getParameter("weight"));
        // Create model
        Cat cat = new Cat(name, breed, weight);
        // Set Model for view
        request.setAttribute("cat", cat);
        // Let view handle the request
        RequestDispatcher view = request.getRequestDispatcher("/WEB-INF/views/showCat.jsp");
        view.forward(request, response);
	}

	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
