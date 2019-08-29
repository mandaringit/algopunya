import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    visitors = sorted(list(map(int, input().split())))

    result = 'Possible'

    for i in range(0, N):
        time = visitors[i]

        fish = (time // M) * K - i

        if fish <= 0:
            result = 'Impossible'
            break

    print("#{} {}".format(tc, result))
