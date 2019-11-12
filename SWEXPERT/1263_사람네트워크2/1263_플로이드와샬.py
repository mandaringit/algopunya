import sys

sys.stdin = open('input.txt', 'r')

# 모든 쌍의 최단 경로를 찾고 그 합을 구하자.
T = int(input())

for tc in range(1, T+1):
    inputs = list(map(int, input().split()))
    N = inputs[0]
    lines = inputs[1:]
    networks = [lines[i*N:i*N+N] for i in range(N)]

    dp = [[1001]*(N+1) for _ in range(N+1)]

    for i in range(N):
        for j in range(N):
            if networks[i][j] == 1:
                dp[i+1][j+1] = 1

    for k in range(1, N+1):
        for i in range(1, N+1):
            if k != i:
                for j in range(1, N+1):
                    if j != i and j != k:
                        dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
    minV = 1000*N
    for i in range(1, N+1):
        total = 0
        for j in range(1, N+1):
            value = dp[i][j]
            if 0 < value < 1001:
                total += value
        if total < minV:
            minV = total
    print("#{} {}".format(tc, minV))
