package com.kevinma.pet.models;

public class Cat extends Animal implements showAffection{
	public Cat(String name, String breed, int weight){
		this.name = name;
		this.breed = breed;
		this.weight = weight;
	}

	@Override
	public String showAffections() {
		return "Your Persian cat, " + this.name + " looked at you with some affection. You think.";
	}
}
