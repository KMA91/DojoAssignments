package com.codingdojo.animal.models;

public class Dog extends Animal{
    public Dog (String name, String breed, int weight){
        this.name = name;
        this.breed = breed;
        this.weight = weight;
    }
	
	public Dog(){
	}
	
	public String showAffection(){
		if(this.weight < 30){
			return (this.name + " hopped into your lamp and cuddled with you!");
		} else {
			return (this.name + " curled up next to you!");
		}
	}

}
