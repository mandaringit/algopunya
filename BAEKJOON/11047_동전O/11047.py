import sys

sys.stdin = open('input.txt', 'r')

# 동전 문제이지만 그리디가 DP보다 빠른 케이스.

N, K = map(int, input().split())

coins = {int(input()): 0 for _ in range(N)}

for coin in list(sorted(coins.keys(), reverse=True)):
    count, rest = divmod(K, coin)

    coins[coin] += count

    K = rest

print(sum(coins.values()))
