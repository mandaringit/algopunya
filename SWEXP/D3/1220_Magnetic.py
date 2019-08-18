for tc in range(1, 11):
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]

    board_col = list(zip(*board))

    count = 0

    for i in range(N):
        row = board_col[i]
        idx = 0
        while idx < N:

            if row[idx] == 1 and idx != N - 1:
                for j in range(idx + 1, N):
                    compare = row[j]

                    if compare == 2:
                        count += 1
                        idx = j + 1
                        break

                    if compare != 2 and j == N - 1:
                        idx = j + 1

            else:
                idx += 1

    print(f"#{tc} {count}")
