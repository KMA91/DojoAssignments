public class BycycleTest {
    public static void main(String[] args) {
        Bycycle b = new Bycycle();
        // print constant
        System.out.println(Bycycle.myConstant);
        b.sayHello();
        Bycycle.staticMethod();
        b.speedUp(3);
        b.applyBrakes(2);
        System.out.println(b.getSpeed());
    }
}