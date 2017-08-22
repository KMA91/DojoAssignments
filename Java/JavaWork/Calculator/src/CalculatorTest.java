
public class CalculatorTest {

	public static void main(String[] args) {
		Calculator c = new Calculator();
		c.performOperation("5");
		c.performOperation("*");
		c.performOperation("6");
		c.performOperation("+");
		System.out.println(c.result);
		System.out.println(c.operandcheck);
		System.out.println(c.operandcheck2);
		c.performOperation("5");
		System.out.println(c.result);
		System.out.println(c.operandcheck);
		System.out.println(c.operandcheck2);
		System.out.println(c.result);
		c.performOperation("=");
	}

}
