package book.javafundamental.ch7;

class Card {
    final int NUMBER;
    final String KIND;
    static int width = 100;
    static int height = 250;

    Card(int NUMBER, String KIND) {
        this.NUMBER = NUMBER;
        this.KIND = KIND;
    }

    Card() {
        this(1, "HEART");
    }

    public String toString() {
        return KIND + " " + NUMBER;
    }
}

class FinalCardTest {
    public static void main(String[] args) {
        Card c = new Card(10, "HEART");
//        c.NUMBER = 5; // 에러
        System.out.println(c.KIND);
        System.out.println(c.NUMBER);
        System.out.println(c);
    }
}
