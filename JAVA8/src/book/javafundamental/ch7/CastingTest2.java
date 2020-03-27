package book.javafundamental.ch7;

public class CastingTest2 {
    public static void main(String[] args) {
        Car car = new Car();
        Car car2 = null;
        FireEngine fe = null;

        car.drive();
        fe = (FireEngine) car; // 실행시 에러
        fe.drive();
        car2 = fe;
        car2.drive();
    }
}
