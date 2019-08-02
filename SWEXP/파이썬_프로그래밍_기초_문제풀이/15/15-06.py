"""
Shape를 부모 클래스로 Square 자식 클래스를 정의하는 코드를 작성하십시오.

Square 클래스는 length 필드를 가지며, 0을 반환하는 Shape 클래스의 area 메서드를

length * length 값을 반환하는 메서드로 오버라이딩합니다.
"""


class Shape:

    def area(self):
        return 0


class Square(Shape):

    def __init__(self,length):
        self.length = length

    def area(self):
        return pow(self.length,2)

    def __str__(self):
        return "정사각형의 면적: {}".format(self.area())


sq1 = Square(5)
print(sq1)
