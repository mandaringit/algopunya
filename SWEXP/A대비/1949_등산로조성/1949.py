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

    return max_height, peaks


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    land = [list(map(int, input().split())) for _ in range(N)]

    max_height, peaks = find_peaks(land, N)

    # for peak in peaks:
