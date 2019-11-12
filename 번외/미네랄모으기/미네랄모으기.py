import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]

    robot = [0, 0]
    minerals = []
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 1:
                robot = [i, j]

            if maps[i][j] > 1:
                minerals.append((i, j))

    dp = [[0]*(C+1) for _ in range(len(minerals)+1)]
    minerals_info = []
    for i, j in minerals:
        E = 2*(abs(robot[0]-i)+abs(robot[1]-j))
        M = maps[i][j]
        minerals_info.append((M, E))

    for i in range(1, len(minerals)+1):
        for pE in range(1, C+1):
            M, E = minerals_info[i-1]
            if pE-E >= 0:
                dp[i][pE] = max(M+dp[i-1][pE-E], dp[i-1][pE])
            else:
                dp[i][pE] = max(0, dp[i-1][pE])

    print(dp[len(minerals)][C])
