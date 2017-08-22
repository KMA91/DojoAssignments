package com.kevinma.pet.models;

public class Dog extends Animal implements showAffection{
	public Dog(String name, String breed, int weight){
		this.name = name;
		this.breed = breed;
		this.weight = weight;
	}

	@Override
	public String showAffections() {
		return this.name + " hopped into your lap and cuddled you!";
		
	}
}
