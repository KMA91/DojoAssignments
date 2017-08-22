package com.codingdojo.animal.models;

public class Cat extends Animal{
	
    public Cat (String name, String breed, int weight){
        this.name = name;
        this.breed = breed;
        this.weight = weight;
    }
	
	public Cat(){
	}
	
	public String showAffection(){
		return "Your " + breed + " cat, " + name + ", looked at you with some affection. You think.";
	}

}
