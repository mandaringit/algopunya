package book.javafundamental.ch7;

import static java.lang.Math.PI;
import static java.lang.Math.random;

public class StaticImportEx1 {
    public static void main(String[] args) {
//        System.out.println(Math.random());
        System.out.println(random());

//        System.out.println("Math.PI : " + Math.PI);
        System.out.println("Math.PI : " + PI);
    }
}
