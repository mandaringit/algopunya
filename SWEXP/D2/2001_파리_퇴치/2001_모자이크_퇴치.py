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

            # 모자이크
            for k in range(M):
                row = board[i + k]

                if k % 2:
                    filtering_row = row[j:j + M:2]
                else:
                    filtering_row = row[j + 1:j + M:2]

                kill += sum(filtering_row)

            if kill > max_kill:
                max_kill = kill

    print(f"#{tc} {max_kill}")
