# import sys
#
# sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    k = int(input())
    n = int(input())

    house = [[0] * 15 for _ in range(15)]
    for i in range(1, 15):
        house[0][i] = i

    for a in range(1, k + 1):
        for b in range(1, n + 1):
            house[a][b] = sum(house[a - 1][1:b + 1])

    print(house[k][n])
