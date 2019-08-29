import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    farm = [list(map(int, list(input()))) for _ in range(N)]

    half = N // 2

    total = 0

    x = 0
    for i in range(N):

        total += sum(farm[i][half - x:half + x + 1])

        if i >= half:
            x -= 1
        else:
            x += 1

    print("#{} {}".format(tc, total))
