import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dp = [[1001]*(N+1) for _ in range(N+1)]

    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        dp[b][a] = 1

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

    counts = [0]*(N+1)
    for i in range(1, N+1):
        for j in range(1, N+1):
            if 0 < dp[i][j] < 1001:
                counts[i] += 1
                counts[j] += 1

    print("#{} {}".format(tc, counts.count(N-1)))
