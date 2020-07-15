import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    dp = [0] * (N + 3)  # 미리 선언할 만큼은있어야 오류가 안남
    dp[1] = 1
    dp[2] = 1

    for i in range(3, N + 1):
        dp[i] = dp[i - 2] + dp[i - 3]

    print(dp[N])
