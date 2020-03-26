package book.javafundamental.ch7;

public class PointerTest2 {
    public static void main(String[] args) {
        Point3d point3d = new Point3d();
        System.out.println("point3d.x=" + point3d.x);
        System.out.println("point3d.=" + point3d.y);
        System.out.println("point3d.z=" + point3d.z);
    }
}

class Point3 {
    int x =10;
    int y = 20;

    Point3 (int x, int y){
        this.x = x;
        this.y = y;
    }

}

class Point3d extends Point3{
    int z = 30;

    Point3d(){
        this(100,200,300);
    }

    Point3d(int x,int y,int z){
        super(x,y);
        this.z = z;
    }
}
