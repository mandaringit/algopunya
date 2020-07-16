import sys

sys.stdin = open('input.txt')

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)  # 1 사분면
elif x > 0 and y < 0:
    print(4)  # 4 사분면
elif x < 0 and y < 0:
    print(3)  # 3 사분면
elif x < 0 and y > 0:
    print(2)  # 2 사분면
