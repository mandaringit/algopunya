import sys

sys.stdin = open('sample_input.txt', 'r')


# 시작 위치, 지금까지 사용한 방향
def cafe_tour(i, j, used_directions):
    # lt lb rt rb  순서로 0 1 2 3
    d = [(-1, -1), (1, -1), (-1, 1), (1, 1)]

    for direction_idx in range(4):
        dx, dy = d[direction_idx]

        ni = i + dx
        nj = j + dy

        # 인덱스 범위 안인가?
        if 0 <= ni < N and 0 <= nj < N:


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    caffes = [list(map(int, input().split()))]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 4방향 제외
            caffe_tour(i, j)
