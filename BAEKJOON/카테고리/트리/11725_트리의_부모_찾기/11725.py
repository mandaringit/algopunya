import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

c1 = [0] * (N + 2)
c2 = [0] * (N + 2)

for _ in range(N - 1):
    p, c = map(int, input().split())

    if c1[p] == 0:
        c1[p] = c
    else:
        c2[p] = c

print(c1)
print(c2)
