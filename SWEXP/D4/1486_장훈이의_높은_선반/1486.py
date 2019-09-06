import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())

    heights = list(map(int, input().split()))

    # 만들 수 있는 높이들
    min_H = sum(heights)
    for i in range(1, 1 << N):
        subset = []
        for j in range(N):
            if i & (1 << j):
                subset.append(heights[j])
        total = sum(subset)
        if B <= total < min_H:
            min_H = total
            if min_H == B:  # 시간 줄이려면 중요
                break

    print("#{} {}".format(tc, min_H - B))
