import sys

sys.stdin = open('input.txt', 'r')


def rep(n):
    global p
    while p[n] != n:
        n = p[n]
    return n


N = int(input())
M = int(input())

edges = []

for _ in range(M):
    edges.append(tuple(map(int, input().split())))
edges.sort(key=lambda x: x[2])

p = [i for i in range(N + 1)]

total_weight = 0
V = 0

for edge in edges:
    n1, n2, cost = edge
    rep1 = rep(n1)
    rep2 = rep(n2)
    if rep1 != rep2:
        total_weight += cost
        p[rep1] = rep2
        V += 1
        if V == N:
            break
print(total_weight)