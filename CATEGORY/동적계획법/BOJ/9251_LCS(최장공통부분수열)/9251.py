import sys

sys.stdin = open('input.txt', 'r')

X = input()
Y = input()

M = len(X)
N = len(Y)

# 0행 -> 0 , 0열 -> 0 (최장길이를 구하기때문)
dp = [[0] * (N + 1) for _ in range(M + 1)]  # 행은 X 열은 Y

for m in range(1, M + 1):
    for n in range(1, N + 1):
        # 1. 0,0 => 0으로 초기화 되있음

        # 2. 만약 인덱스가 동일한 두 글자가 같다면
        if X[m - 1] == Y[n - 1]:
            dp[m][n] = dp[m - 1][n - 1] + 1  # 해당 두 단어의 최장길이수열은 Xm-1,Yn-1보다 1 길다.

        # 3. 만약 인덱스가 동일한 두 글자가 다르다면
        else:
            # 해당 두 단어의 최장길이수열은
            # Xm,Yn-1의 LCS길이와 Xm-1,Yn의 LCS길이 중 큰 값이다.
            dp[m][n] = max(dp[m - 1][n], dp[m][n - 1])

print(dp[M][N])
