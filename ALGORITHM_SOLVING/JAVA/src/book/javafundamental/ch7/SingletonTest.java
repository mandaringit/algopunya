package book.javafundamental.ch7;

final class Singleton {
    private static Singleton s = new Singleton();

    private Singleton() {
        // ..
    }

    public static Singleton getInstance() {
        if (s == null) {
            s = new Singleton();
        }
        return s;
    }
}

public class SingletonTest {
    public static void main(String[] args) {
//        Singleton s = new Singleton(); // 에러
        Singleton s = Singleton.getInstance();
    }
}
