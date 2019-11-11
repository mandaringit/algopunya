import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    carrots = [0] + list(map(int, input().split()))

    d = 0
    w = 0
    for i in range(1, N + 1):
        d += 1

        if carrots[i] + w <= M:  # 여유
            w += carrots[i]
            carrots[i] = 0

        else:
            # 일단 수레에 다 채운다
            while carrots[i] >= M - w:
                possible = M - w
                carrots[i] = carrots[i] - possible
                # 비우고 옴
                d += i * 2
                w = 0
            w = carrots[i]
            carrots[i] = 0

    print(f"#{tc} {d + N}")
