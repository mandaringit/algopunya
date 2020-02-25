import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
numbers = list(map(int, input().split()))

dp = [0] * N

for i in range(N):
    value = 0
    for j in range(0, i):
        if numbers[i] > numbers[j]:
            value = max(value, dp[j])

    dp[i] = value + 1
print(max(dp))
