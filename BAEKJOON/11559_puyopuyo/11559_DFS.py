import sys

sys.stdin = open('input.txt', 'r')


def DFS(i, j):
    global field, visited, count

    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visited[i][j] = 1
    path = [(i, j)]
    stack = [(i, j)]
    color = field[i][j]
    while stack:
        i_, j_ = stack.pop()

        for dx, dy in d:
            ni = i_ + dx
            nj = j_ + dy

            if 0 <= ni < 12 and 0 <= nj < 6:
                if field[ni][nj] == color and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    path.append((ni, nj))
                    stack.append((ni, nj))

    if len(path) >= 4:  # 각각을 폭발시킨다
        for i_, j_ in path:
            field[i_][j_] = '.'
        count += 1
        return


# 해당 col을 정렬한다
def align(col):
    global field

    column = ''

    # 해당 열 복사하기
    for i in range(12):
        value = field[i][col]
        column += value

    column = column.replace('.', '')
    padding = 12 - len(column)
    column = '.' * padding + column

    if padding != 0:
        for i in range(12):
            field[i][col] = column[i]


field = [list(input()) for _ in range(12)]
boom = 0

while True:
    visited = [[0] * 6 for _ in range(12)]
    count = 0  # 폭발하는 군집 수
    for i in range(12):
        for j in range(6):
            if field[i][j] in ['R', 'G', 'B', 'P', 'Y'] and visited[i][j] == 0:
                DFS(i, j)  # 군집 찾아 폭발

    # 각 열들을 다시 정렬
    for i in range(6):
        align(i)

    if count == 0:  # 폭발한게 하나도 없으면 끝
        break
    else:
        boom += 1

print(boom)
