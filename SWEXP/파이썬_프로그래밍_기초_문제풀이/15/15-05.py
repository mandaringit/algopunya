"""
가로, 세로 정보을 갖고, 사각형의 면적을 계산하는 메서드를 갖는 Rectangle 클래스를 정의하고,

생성한 객체의 사각형의 면적을 출력하는 프로그램을 작성하십시오.
"""

class Rectangle:
    def __init__(self,length,height):
        self.length = length
        self.height = height

    def calc_rectangle_area(self):
        return self.height * self.length

    def __str__(self):
        return "사각형의 면적: {}".format(self.calc_rectangle_area())

rec1 = Rectangle(5,4)
print(rec1)