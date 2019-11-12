import sys

sys.stdin = open('sample_input.txt', 'r')


def DFS(i, j, cutting, path_count):
    global visited, N, K, maps, maxPath
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visited[i][j] = 1
    path_count += 1

    if path_count > maxPath:
        maxPath = path_count

    h = maps[i][j]
    for dx, dy in d:
        ni = i+dx
        nj = j+dy

        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            nh = maps[ni][nj]
            if h > nh:
                DFS(ni, nj, cutting, path_count)
            else:
                if h > nh-K and cutting == 1:
                    origin = maps[ni][nj]
                    maps[ni][nj] = h-1  # 최소한으로 깎는다
                    DFS(ni, nj, 0, path_count)
                    maps[ni][nj] = origin
    visited[i][j] = 0


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]

    maxValue = 0
    for i in range(N):
        value = max(maps[i])
        if value > maxValue:
            maxValue = value

    peaks = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == maxValue:
                peaks.append((i, j))

    maxPath = 0
    visited = [[0]*N for _ in range(N)]
    for i, j in peaks:
        DFS(i, j, 1, 0)
    print("#{} {}".format(tc, maxPath))
