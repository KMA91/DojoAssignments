package com.teamroster.models;

public class Player implements java.io.Serializable{
	private String first_name;
	private String last_name;
	private int age;
	
	public Player(){
	}
	
	public Player(String first_name, String last_name, int age){
		this.first_name = first_name;
		this.last_name = last_name;
		this.age = age;
	}
}
