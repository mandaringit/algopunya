package book.javafundamental.ch6;

// 스태틱은 인스턴스 메서드 / 변수를 부를수 없다.
// 인스턴스는 스태틱을 부를 수 있다.
class MemberCall {
    int iv = 10;
    static int cv = 20;

    int iv2 = cv;
    //    static int cv2 = iv;
    static int cv2 = new MemberCall().iv;

    static void staticMethod1() {
        System.out.println(cv);
//        System.out.println(iv);
        MemberCall mc = new MemberCall();
        System.out.println(mc.iv);
    }

    void instanceMethod1() {
        System.out.println(cv);
        System.out.println(iv);
    }

    static void staticMethod2() {
        staticMethod1();
//        instanceMethod1();
        MemberCall mc = new MemberCall();
        mc.instanceMethod1();
    }

    void instanceMethod2(){
        staticMethod1();
        instanceMethod1();
    }
}
