
public class Samurai extends Human{

	public static Integer count = 0;
	
	public Samurai() {
		this.health = 200;
		count += 1;
	}
	
	public void deathBlow(Human victim){
		victim.health = 0;
		this.health /= 2;
		System.out.println("Samurai destroyed a victim. Health is cut in half!");
	}
	
	public void meditate(){
		System.out.println("Samurai healed for " + this.health/2 + "!");
		this.health += this.health/2;
	}
	
	public String howMany(){
		return count + " samurais!";
	}

}