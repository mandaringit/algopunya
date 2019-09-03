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


def explore(i, j, count):
    global land
    global N
    global K
    global peaks
    global max_root

    if count > max_root:
        max_root = count

    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in d:
        ni = i + dx
        nj = j + dy

        if 0 <= ni < N and 0 <= nj < N:
            if land[ni][nj] < land[i][j]:
                explore(ni, nj, count + 1)


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]
    peaks = find_peaks(land, N)
    max_root = 0

    for i, j in peaks:
        explore(i, j, 1)

    print("#{} {}".format(tc, max_root))
