import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    X, Y = input().split()

    M = len(X)
    N = len(Y)

    dp = [[0] * (N + 1) for _ in range(M + 1)]

    for m in range(1, M + 1):
        for n in range(1, N + 1):

            if X[m - 1] == Y[n - 1]:
                dp[m][n] = dp[m - 1][n - 1] + 1
            else:
                dp[m][n] = max(dp[m - 1][n], dp[m][n - 1])

    print("#{} {}".format(tc, dp[M][N]))
