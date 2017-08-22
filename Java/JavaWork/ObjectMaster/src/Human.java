public class Human {
	protected Integer health = 100;
	protected Integer strength = 3;
	protected Integer stealth = 3;
	protected Integer intelligence = 3;
	
	public void attack(Human defender){
		defender.health -= this.strength;
	}
}
