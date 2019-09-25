def check_row(N, K, board):
    row_count = 0

    for row in board:
        count = 0
        for idx, cell in enumerate(row):
            if cell:
                count += 1
                if count == K:
                    if idx == N - 1 or not row[idx + 1]:
                        row_count += 1
            else:
                count = 0
    return row_count


def check_column(N, K, board):
    zip_column = list(zip(*board))  # 매우 혁신적이다.

    return check_row(N, K, zip_column)


T = int(input())
result = []

for t in range(1, T + 1):
    N, K = map(int, input().split())

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    row_count = check_row(N, K, board)
    column_count = check_column(N, K, board)
    result.append(f"#{t} {row_count + column_count}")
print("\n".join(result))
