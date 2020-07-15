import sys

sys.stdin = open('s_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    D, A, B, F = map(int, input().split())

    sec = D / (A + B)

    fly = sec * F

    print("#{} {}".format(tc, fly))
