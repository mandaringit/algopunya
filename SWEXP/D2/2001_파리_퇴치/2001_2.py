import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0
    # 가능 범위 -> 0 ~ N - M 까지
    for i in range(0, N - M + 1):
        for j in range(0, N - M + 1):

            kill = 0
            # 파리채 범위 -> i ~ i + M -1
            for k in range(i, i + M):
                for m in range(j, j + M):
                    kill += board[k][m]

            if kill > max_kill:
                max_kill = kill

    print(f"#{tc} {max_kill}")



