'''
반지름 정보를 갖고, 원의 면적을 계산하는 메서드를 갖는 Circle 클래스를 정의하고,

생성한 객체의 원의 면적을 출력하는 프로그램을 작성하십시오.
'''


class Circle :

    def __init__(self,radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    def calc_circle_area(self):
        return 3.14 * pow(self.radius,2)

    def __str__(self):
        return "원의 면적: {}".format(self.calc_circle_area())

circle1 = Circle(2)
print(circle1)