
public class HumanTest {

	public static void main(String[] args) {
		Human h1 = new Human();
		Human h2 = new Human();
		h1.attack(h2);
		Ninja n = new Ninja();
		Wizard w = new Wizard();
		Samurai s = new Samurai();
		Samurai s2 = new Samurai();
		n.steal(w);
		n.runAway();
		w.heal(s);
		w.fireball(n);
		s.deathBlow(w);
		s.meditate();
		System.out.println(s.howMany());
	}
}
