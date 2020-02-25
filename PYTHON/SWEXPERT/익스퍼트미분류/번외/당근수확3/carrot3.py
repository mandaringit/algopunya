import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 행, 열
    carrots = [list(map(int, input().split())) for _ in range(N)]

    min_diff = 0
    for i in range(N):
        min_diff += sum(carrots[i])

    for i in range(1, N):  # 위, 아래
        for j in range(1,M):  # 좌, 우

            area1 = 0
            area2 = 0
            area3 = 0

            for k in range(0, i):
                area1 += sum(carrots[k][:j])
                area2 += sum(carrots[k][j:])

            for k in range(i, N):
                area3 += sum(carrots[k])

            diff = max(abs(area1 - area2), abs(area1 - area3), abs(area2 - area3))

            if diff < min_diff:
                min_diff = diff

    print(f"#{tc} {min_diff}")
