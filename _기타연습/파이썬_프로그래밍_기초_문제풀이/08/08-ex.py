# 원의 면적과 원의 둘레를 구하는 프로그램을 작성하라

PI = 3.14

def input_radius():
    radius_input = input("반지름을 입력하세요 : ")
    return float(radius_input)


def calc_circle_area(r):
    return PI * r * r

def calc_circumference(r):
    return 2 * PI * r

radius = input_radius()
circle_area = calc_circle_area(radius)
circumference = calc_circumference(radius)

print("원의 넓이 : {0:0.2f} , 원의 둘레 : {1:0.2f}".format(circle_area,circumference))