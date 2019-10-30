import sys

sys.stdin = open('sample_input.txt', 'r')


def DFS(i, j, count, drill):
    global visited, N, maps, maxPath, K

    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    if count > maxPath:
        maxPath = count

    visited[i][j] = 1

    for dx, dy in d:
        ni = i + dx
        nj = j + dy

        # 1. 범위 안이고
        if 0 <= ni < N and 0 <= nj < N:
            # 2-1. 자신보다 높이가 작은곳이면
            if maps[ni][nj] < maps[i][j] and not visited[ni][nj]:
                DFS(ni, nj, count + 1, drill)  # 탐색

            # 2-2. 자신보다 큰곳이고, 아직 안갔고, 공사 가능하면
            elif maps[ni][nj] - K < maps[i][j] <= maps[ni][nj] and not visited[ni][nj] and drill:
                origin = maps[ni][nj]
                maps[ni][nj] -= K
                DFS(ni, nj, count + 1, 0)
                maps[ni][nj] = origin

    visited[i][j] = 0


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    # 시작점 찾기.
    maxPath = 0
    starts = []

    maxH = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] > maxH:
                maxH = maps[i][j]

    for i in range(N):
        for j in range(N):
            if maps[i][j] == maxH:
                peak = [i, j, maps[i][j]]
                starts.append(peak)

    for peak in starts:
        DFS(peak[0], peak[1], 1, 1)
    print(f"#{tc} {maxPath}")
