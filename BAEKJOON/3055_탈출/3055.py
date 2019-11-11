import sys

sys.stdin = open('input.txt', 'r')


def BFS(start_q):
    global forest
    global goal
    global R, C

    while start_q:
        i, j, typ = start_q.pop(0)

        if (i, j) == goal:
            return typ

        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in d:
            ni = i + dx
            nj = j + dy

            if 0 <= ni < R and 0 <= nj < C:
                adj_value = forest[ni][nj]
                # 시작하는 놈이 물이고, 인접지역이 '.' 또는 숫자일때
                if typ == '*' and adj_value != 'X' and adj_value != 'D' and adj_value != '*':
                    forest[ni][nj] = '*'  # 인접 지역을 물로 변경
                    start_q.append([ni, nj, typ])

                # 고슴도치이고 , 주변이 돌,물,이미 갔던곳 아니면
                if isinstance(typ, int) and adj_value != 'X' and adj_value != '*' and not isinstance(adj_value, int):
                    forest[ni][nj] = typ + 1
                    if (ni, nj) == goal:
                        return typ + 1
                    else:
                        start_q.append([ni, nj, typ + 1])

    return 'KAKTUS'


R, C = map(int, input().split())
forest = [list(input()) for _ in range(R)]
waters = []
for i in range(R):
    for j in range(C):
        if forest[i][j] == 'D':
            goal = (i, j)
        if forest[i][j] == 'S':
            start = (i, j, 0)
            forest[i][j] = 0  # 출발점을 0으로 표시해주기
        if forest[i][j] == '*':
            waters += [(i, j, '*')]
q = []
q.extend(waters + [start])  # 물먼저 이동시키고 그 다음 고슴도치 이동
print(BFS(q))
