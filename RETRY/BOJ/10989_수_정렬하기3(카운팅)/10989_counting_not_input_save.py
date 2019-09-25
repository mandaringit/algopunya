import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

counting = [0] * 10001

for _ in range(N):
    counting[int(input())] += 1

B = []

for i in range(10001):
    if counting[i] > 0:
        for j in range(counting[i]):
            B.append(i)

for num in B:
    print(num)
