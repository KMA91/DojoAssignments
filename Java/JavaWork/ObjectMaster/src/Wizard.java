
public class Wizard extends Human{

	public Wizard() {
		this.health = 50;
		this.intelligence = 8;
	}
	
	public void heal(Human friend){
		friend.health += this.intelligence;
		System.out.println("Wizard healed a friend!");
	}
	
	public void fireball(Human victim){
		victim.health -= this.intelligence*3;
		System.out.println("Wizard fireballed a victim!");
	}

}
