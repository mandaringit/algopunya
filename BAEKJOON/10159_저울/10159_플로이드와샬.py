import sys

sys.stdin = open('input.txt', 'r')

# expert 키 순서 문제랑 동일함

N = int(input())
M = int(input())

dp = [[2001]*(N+1) for _ in range(N+1)]  # 최대 2000

for _ in range(M):
    n1, n2 = map(int, input().split())
    dp[n1][n2] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        if i != k:
            for j in range(1, N+1):
                if j != k and j != i:
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

counts = [0]*(N+1)
for i in range(1, N+1):
    for j in range(1, N+1):
        if dp[i][j] < 2001:
            counts[i] += 1
            counts[j] += 1

for value in counts[1:]:
    print(N-value-1)  # 전체노드수 - 알수있는 노드수 - 1(자기자신)
