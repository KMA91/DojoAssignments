
public class Ninja extends Human{

	public Ninja() {
		this.stealth = 10;
	}

	public void steal(Human victim){
		victim.health += this.stealth;
		this.health += this.stealth;
		System.out.println("Ninja stole from a victim");
	}
	
	public void runAway(){
		this.health -= 10;
		System.out.println("Ninja ran away!");
	}
}
