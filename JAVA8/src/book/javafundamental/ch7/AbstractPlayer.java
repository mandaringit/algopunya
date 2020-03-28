package book.javafundamental.ch7;

abstract class Player {
    abstract void play(int pos);

    abstract void stop();
}

class AudioPlayer extends Player {
    @Override
    void play(int pos) {

    }

    @Override
    void stop() {

    }
}

abstract class AbstractPlayer extends Player {
    void play(int pos){

    }
}
