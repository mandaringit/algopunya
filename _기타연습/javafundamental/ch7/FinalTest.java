package book.javafundamental.ch7;

final class FinalTest { // 조상 불가 클래스
    final int MAX_SIZE = 10;

    final int getMaxSize(){
        final int LV = MAX_SIZE;
        return LV;
    }
}
