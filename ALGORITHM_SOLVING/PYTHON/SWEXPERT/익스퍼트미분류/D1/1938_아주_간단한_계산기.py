# 테스트에선 eval이 허용이 안됨
a, b = (int(num) for num in input().split())
operators = ["+", "-", "*", "/"]
for op in operators:
    if op == "+":
        print(a+b)
    elif op == '-':
        print(a-b)
    elif op == '/':
        print(a//b)
    else:
        print(a*b)
