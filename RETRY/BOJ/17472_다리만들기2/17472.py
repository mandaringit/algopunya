import sys

sys.stdin = open('input.txt', 'r')


def dividing(i, j, count):
    global maps, N, M
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    stack = [(i, j)]
    maps[i][j] = count

    while stack:
        i_, j_ = stack.pop()

        for dx, dy in d:
            ni = i_+dx
            nj = j_+dy

            if 0 <= ni < N and 0 <= nj < M:
                if maps[ni][nj] == 1:
                    maps[ni][nj] = count
                    stack.append((ni, nj))


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]

    # 섬 구분
    count = 1  # 섬번호는 2번부터 매기자
    adj = {}
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 1:
                count += 1
                dividing(i, j, count)

    for row in maps:
        for idx, value in enumerate(row):
