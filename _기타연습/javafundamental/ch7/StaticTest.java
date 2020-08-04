package book.javafundamental.ch7;

public class StaticTest {
    static int width = 200;
    static int height = 120;

    static {
        // static 변수의 복잡한 초기화 수행
    }

    static int max(int a, int b) {
        return a > b ? a : b;
    }
}
