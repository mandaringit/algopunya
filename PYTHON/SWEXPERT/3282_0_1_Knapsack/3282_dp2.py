import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    dp = [[0]*(K+1) for _ in range(N+1)]

    for i in range(1, N+1):
        V, C = map(int, input().split())

        for Volume in range(1, K+1):  # v는 가능한 부피
            if Volume-V >= 0:  # 나를 넣을 수 있으면
                dp[i][Volume] = max(C+dp[i-1][Volume-V], dp[i-1][Volume])
            else:
                dp[i][Volume] = max(0, dp[i-1][Volume])

    print(dp)
