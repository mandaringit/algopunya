import sys

sys.stdin = open('sample_input.txt', 'r')

# 이 문제도 순열로 가능한 문제다. 다만 백트래킹 문제라 시간초과가 난다.

def permutation(n, k):
    global costs
    global N
    global factories
    global minV

    if n == k:
        total_cost = 0
        for i in range(N):
            total_cost += costs[i][factories[i]]
        if total_cost < minV:
            minV = total_cost
    else:
        for i in range(n, k):
            factories[n], factories[i] = factories[i], factories[n]
            permutation(n + 1, k)
            factories[n], factories[i] = factories[i], factories[n]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    costs = [list(map(int, input().split())) for _ in range(N)]
    factories = [i for i in range(N)]
    minV = 99 * N
    permutation(0, N)

    print("#{} {}".format(tc, minV))
