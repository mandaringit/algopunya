
# ㄷ

def diguet_filter(i, j, k, m, M):
    return i + 1 <= k < i + M - 1 and j + 1 <= m < j + M


import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0

    for i in range(0, N - M + 1):
        for j in range(0, N - M + 1):

            kill = 0

            for k in range(i, i + M):
                for m in range(j, j + M):

                    if diguet_filter(i, j, k, m, M):
                        pass
                    else:
                        kill += board[k][m]

            if kill > max_kill:
                max_kill = kill

    print(f"#{tc} {max_kill}")
