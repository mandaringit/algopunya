# 팩토리얼
# 0! = 1 이다


def factorial(n):
    if 0 <= n <= 1:
        return 1
    else:
        return n * factorial(n-1)


number = int(input())
print(factorial(number))
