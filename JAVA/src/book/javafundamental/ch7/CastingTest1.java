package book.javafundamental.ch7;

public class CastingTest1 {
    public static void main(String[] args) {
        Car car = null;
        FireEngine fe = new FireEngine();
        FireEngine fe2 = null;

        fe.water();
        car = fe; // UpCasting . (Car)fe 에서 (Car) 생략
//        car.water(); // error
        fe2 = (FireEngine) car; // DownCasting
        fe2.water();
    }
}

class Car {
    String color;
    int door;

    void drive() {
        System.out.println("drive, brrr~");
    }

    void stop() {
        System.out.println("stop!");
    }
}

class FireEngine extends Car {
    void water() {
        System.out.println("water");
    }
}
