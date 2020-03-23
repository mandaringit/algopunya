package book.javafundamental.ch6;

public class TvTest3 {
    public static void main(String[] args) {
        Tv tv1 = new Tv();
        Tv tv2 = new Tv();
        System.out.println("tv1의 channel 값은  " + tv1.channel + " 입니다.");
        System.out.println("tv2의 channel 값은  " + tv2.channel + " 입니다.");

        tv2 = tv1; // tv2가 이제 tv1 의 주소를 가리킨다.
        tv1.channel = 7;
        System.out.println("tv1의 channel 값을 7로 변경하였습니다.");
        System.out.println("tv1의 channel 값은 " + tv1.channel + " 입니다.");
        System.out.println("tv2의 channel 값은 " + tv2.channel + " 입니다.");
    }
}
