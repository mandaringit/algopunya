# 시간초과쓰 왜냐 ? 모두 검사하니까..

import sys

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())

cards = list(map(int, input().split()))

max_sum = 0

for i in range(1, 1 << N):
    subset = []
    for j in range(N):
        if i & (1 << j):
            subset.append(cards[j])

    if len(subset) == 3:
        total = sum(subset)
        if max_sum < total <= M:
            max_sum = total
    if max_sum == M:
        break

print(max_sum)