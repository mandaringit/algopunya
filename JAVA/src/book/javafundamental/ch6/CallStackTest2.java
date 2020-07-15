package book.javafundamental.ch6;

public class CallStackTest2 {
    public static void main(String[] args) {
        System.out.println("main(String[] args)이 시작되었음.");
        firstMethod();
        System.out.println("main(String[] args)이 끝났음");
    }

    static void firstMethod() {
        System.out.println("firstMehtod()이 시작되었음");
        secondMethod();
        System.out.println("firstMehtod()이 끝났음");
    }

    static void secondMethod() {
        System.out.println("secondMehtod()이 시작되었음");
        System.out.println("secondMehtod()이 끝났음");
    }

}
