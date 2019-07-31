# 빠르게 입력받기!!
import sys

T = int(input())
for _ in range(T):
    a, b = tuple(map(int, sys.stdin.readline().split()))
    print(a+b)
