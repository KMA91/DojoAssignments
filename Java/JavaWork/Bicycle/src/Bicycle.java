class Bycycle implements OperateBycycle {       
    private int speed;
    public Bycycle() {
        speed = 0;
    }
    // a static method that calls on the interface static method
    public static void staticMethod() {
        OperateBycycle.staticMethod();
    }
    // implementing speedUp
    public void speedUp(int increment) {
        speed += increment;
    }
    // implementing applyBrakes
    public void applyBrakes(int decrement) {
        speed -= decrement;
    }
    public int getSpeed() {
        return speed;
    }
}