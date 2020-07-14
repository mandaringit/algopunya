import sys

sys.stdin = open('sample_input.txt', 'r')


def find_peaks(land, N):
    peaks = []
    max_height = 0

    for i in range(N):
        for j in range(N):
            if land[i][j] > max_height:
                max_height = land[i][j]
                peaks = [[i, j]]
            elif land[i][j] == max_height:
                peaks.append([i, j])

    return peaks


def explore(i, j, drill, count):
    global max_root
    global visited

    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visited[i][j] = 1

    if count > max_root:
        max_root = count

    for dx, dy in d:
        ni = i + dx
        nj = j + dy

        if 0 <= ni < N and 0 <= nj < N:
            # 안깎아도 되는 경우 방문여부를 확인 안해도 상관없는 이유는 어차피 높은곳에서 내려오기 때문.
            if land[ni][nj] < land[i][j]:
                explore(ni, nj, drill, count + 1)

            # 깎아야하는경우, 방문여부를 확인하는 이유는 다른 높은곳에서부터 내려오는데,
            # 돌다가 상하좌우중 이미 방문한곳을 깎고 갈 위험이 있기 때문.
            elif visited[ni][nj] == 0 and land[ni][nj] - K < land[i][j] and drill:
                original = land[ni][nj]
                land[ni][nj] = land[i][j] - 1
                explore(ni, nj, 0, count + 1)
                land[ni][nj] = original

    visited[i][j] = 0


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    land = [list(map(int, input().split())) for _ in range(N)]

    peaks = find_peaks(land, N)

    max_root = 0
    visited = [[0] * N for _ in range(N)]

    for i, j in peaks:
        explore(i, j, 1, 1)

    print("#{} {}".format(tc,max_root))
