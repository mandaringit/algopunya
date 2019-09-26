import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    stuffs = [tuple(map(int, input().split())) for _ in range(N)]
    maxC = 0
    for i in range(1, 1 << N):
        subset = []
        for j in range(N):
            if i & (1 << j):
                subset.append(stuffs[j])

        V = sum(map(lambda x: x[0], subset))
        C = sum(map(lambda x: x[1], subset))

        if V <= K and C > maxC:
            maxC = C

    print("#{} {}".format(tc, maxC))
