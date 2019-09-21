import sys

sys.stdin = open('input.txt', 'r')


"@.com"

T = int(input())

for tc in range(1, T + 1):
    a = input()

    print(solution(a))
