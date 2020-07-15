def isWall(row, col, arr, N):
    if 0 <= row <= N - 1 and 0 <= col <= N - 1 and arr[row][col] == 0:
        return False
    else:
        return True


def changeDirection(direction):
    return (direction + 1) % 4


T = int(input())
for t in range(1, 1 + T):
    N = int(input())

    arr = []

    for i in range(N):
        arr.append([0] * N)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    direction = 0
    row = 0
    col = 0

    for i in range(1, N * N + 1):
        arr[row][col] = str(i)

        row_move = directions[direction][0]
        col_move = directions[direction][1]

        row += row_move
        col += col_move

        if isWall(row + row_move, col + col_move, arr, N):
            direction = changeDirection(direction)

    print(f"#{t}")

    for line in arr:
        print(" ".join(line))
