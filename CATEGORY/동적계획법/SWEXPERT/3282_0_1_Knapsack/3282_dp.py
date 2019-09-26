import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    stuffs = [0] + [tuple(map(int, input().split())) for _ in range(N)]  # 물건 번호가 1 ~ N이 되게끔
    dp = [[0] * (K + 1) for _ in range(N + 1)]  # 최댓값을 구하므로 위쪽 왼쪽에 0을 기본값으로

    for i in range(1, N + 1):
        for j in range(1, K + 1):  # 여기서 j는 최대로 넣을 수 있는 부피가 된다.
            v = stuffs[i][0]  # i 번째의 부피
            c = stuffs[i][1]  # i 번째의 가치

            # i 번째가 포함될때의 가치 =
            # 못넣을때(v > j) -> i번째 부피가 j보다 작으면 못 넣는 것이니까 0
            # 넣을때 ->
            # 1. 자신의 가치 c
            # 2. 자신을 넣을 수 있는 부피(j - v)이면서 i 이전의 dp중 가장 큰값
            # dp[i번째 이전][현재 넣을 수 있는 부피 - i번째의 부피]
            # => dp[i-1][j - v]
            im_included = 0 if v > j else c + dp[i - 1][j - v]

            # dp[i][j] = max(자신이 포함될때, 포함 안됬을때)
            dp[i][j] = max(im_included, dp[i - 1][j])

    print("#{} {}".format(tc, dp[N][K]))
