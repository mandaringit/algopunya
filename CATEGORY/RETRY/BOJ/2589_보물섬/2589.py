import sys

sys.stdin = open('input.txt', 'r')


# 시간초과

def get_islands(i, j, count):
    global treasure_map
    global islands

    stack = [[i, j]]
    treasure_map[i][j] = count
    while stack:
        i_, j_ = stack.pop()

        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in d:
            ni = i_ + dx
            nj = j_ + dy

            if 0 <= ni < N and 0 <= nj < M:
                if treasure_map[ni][nj] == 'L':
                    treasure_map[ni][nj] = count
                    islands[count].append([ni, nj])
                    stack.append([ni, nj])


def BFS(start, goal, island_number):
    global treasure_map, N, M
    global maxV
    visited = [[-1] * M for _ in range(N)]

    q = [start]

    visited[start[0]][start[1]] = 0

    while q:

        i, j = q.pop(0)

        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in d:
            ni = i + dx
            nj = j + dy

            if 0 <= ni < N and 0 <= nj < M:
                if treasure_map[ni][nj] == island_number and visited[ni][nj] == -1:
                    visited[ni][nj] = visited[i][j] + 1

                    if [ni, nj] == goal:
                        move_time = visited[ni][nj]
                        if move_time > maxV:
                            maxV = move_time
                        return

                    else:
                        q.append([ni, nj])


N, M = map(int, input().split())

treasure_map = [list(input()) for _ in range(N)]

islands = {}

count = 0
for i in range(N):
    for j in range(M):
        if treasure_map[i][j] == 'L':
            count += 1
            islands[count] = []
            get_islands(i, j, count)

maxV = 0
for island in islands:
    lands = islands[island]

    for i in range(len(lands)):
        for j in range(i + 1, len(lands)):
            # print(lands[i], lands[j], island)  # 출발 , 도착 경우들
            BFS(lands[i], lands[j], island)

print(maxV)
