# 부동 소수점은 이진수 분수로 표현되므로 함부로 비교하거나 빼면 안된다.
# 0.1처럼.. 2진수로 표현하기 어려운 숫자가 있다..
print("0.2 * 3 == 0.6", 0.2 * 3 == 0.6)
print("1.2 - 0.2 == 1.0", 1.2 - 0.2 == 1.0)
print("1.2 - 0.1 == 1.1", 1.2 - 0.1 == 1.1)
print("0.1 * 0.1 == 0.01", 0.1 * 0.1 == 0.01)


# 동등성 테스트 접근법
def a(x, y, places=7):
    return round(abs(x - y), places) == 0


# 정수, 부동 소수점 메서드
print(divmod(45, 6))
print(round(113.866, -1))  # 음수의 경우, 정수 n번째 자리에서 반올림
print(round(113.866, 2))  # 양수인경우, 소수점 이하 n번째 자리에서 반올림

print(2.75.as_integer_ratio())  # 부동 소숫점을 분수로 표현
print(3.5.as_integer_ratio())


