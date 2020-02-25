import sys

sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())

dp = [[0] * (K + 1) for _ in range(N + 1)]
stuffs = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        # i,j 의 dp값은 무엇이냐하 ~
        # i번 째의..
        weight = stuffs[i - 1][0]
        value = stuffs[i - 1][1]

        # i번째가 가능한 부피(j)라면, 자신의 가치 + (j-weight)의 i-1의 dp값
        # 불가능하다면, i-1번째의 dp값.
        # 위 두 값중 최대값.

        im_include_value = 0
        possible_weight = j - weight

        if possible_weight >= 0:
            im_include_value += value + dp[i - 1][possible_weight]

        dp[i][j] = max(im_include_value, dp[i - 1][j])
print(dp[N][K])
