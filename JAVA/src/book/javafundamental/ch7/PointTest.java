package book.javafundamental.ch7;

class Point2 {
    int x;
    int y;

    Point2(int x,int y){
        this.x = x;
        this.y = y;
    }

    String getLocation(){
        return "x :" + x + ", y:" + y;
    }
}

class Point3D extends Point2{
    int z;

    Point3D(int x, int y, int z) {
        super(x, y);
        this.z = z;
    }

    String getLocation() {
        return "x :" + x + ", y :" + y + ", z :" + z;
    }
}

public class PointTest {
    public static void main(String[] args) {
        Point3D point3D = new Point3D(1, 2, 3);
    }
}
