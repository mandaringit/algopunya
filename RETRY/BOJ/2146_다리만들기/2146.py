import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

boundaries = []
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 일단 섬을 구분???해야하나 ??

for i in range(N):
    for j in range(N):

        if maps[i][j] == 1:
            for dx, dy in d:
                ni = i + dx
                nj = j + dy

                if 0 <= ni < N and 0 <= nj < N:
                    if maps[ni][nj] == 0:  # 하나라도 바다가 있으면
                        boundaries.append((i, j))
                        break

start = boundaries[0]
visited = [[-1] * N for _ in range(N)]
visited[start[0]][start[1]] = 0
new_boundaries = boundaries[1:]

while new_boundaries:
    i, j = new_boundaries.pop(0)

    for dx, dy in d:
        ni = i + dx
        nj = j + dy

        if 0 <= ni < N and 0 <= nj < N:
            if visited[ni][nj] == -1 and maps[ni][nj] == 0:
                visited[ni][nj] = visited[i][j] + 1
                new_boundaries.append((ni,nj))
            elif visited[ni][nj] >= 0: # 만나긴 만났는데... 옆에 만나면 어떡하지

