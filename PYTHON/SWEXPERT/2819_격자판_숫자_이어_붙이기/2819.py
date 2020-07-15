import sys

sys.stdin = open('sample_input.txt', 'r')


def explore(i, j, count, path):
    global paths
    global board

    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    if count == 6:
        paths.add(tuple(path))

    else:
        for dx, dy in d:

            ni = i + dx
            nj = j + dy

            if 0 <= ni < 4 and 0 <= nj < 4:
                explore(ni, nj, count + 1, path + [board[ni][nj]])


T = int(input())

for tc in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(4)]
    paths = set()
    for i in range(4):
        for j in range(4):
            explore(i, j, 0, [board[i][j]])

    print("#{} {}".format(tc, len(paths)))
