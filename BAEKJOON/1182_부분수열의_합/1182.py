import sys

sys.stdin = open('input.txt', 'r')

N, S = map(int, input().split())

numbers = list(map(int, input().split()))

count = 0
for i in range(1, 1 << N):
    total = 0
    for j in range(N):
        if i & (1 << j):
            total += numbers[j]

    if total == S:
        count += 1

print(count)
