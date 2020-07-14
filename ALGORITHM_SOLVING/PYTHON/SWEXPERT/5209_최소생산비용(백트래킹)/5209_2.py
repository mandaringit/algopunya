"""
5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용
을 이렇게 풀어보세요.

물건을 주문하는 지역 좌표(i1, j1)와 각 공장의 위치 좌표(i2, j2)가 주어진다.
물건을 만드는 비용은 지역과 공장의 거리(|i1-i2|+|j1-j2|)로 결정된다면,
각 물건을 생산하는 최소 비용은 얼마인가? 한 공장에서 한 개의 물건만
생산한다.
N과 N개의 지역 좌표, N개 공장의 좌표가 차례로 주어진다.
(3<=N<=7,  -100<=i, j<=100)
3
-24	-3
-59	5
-2	-79
25	-15
-15	71
-99	-92
"""

import sys

sys.stdin = open('2_input.txt', 'r')


def DFS(p, cost, visited_factory):
    global adj
    global N
    global minV
    global all_factories

    if p == N - 1:
        if cost < minV:
            minV = cost
    elif cost > minV:
        return
    else:
        for factory in all_factories - visited_factory:
            DFS(p + 1, cost + adj[p + 1][factory], visited_factory | {factory})


N = int(input())
locs = [list(map(int, input().split())) for _ in range(N)]
factories = [list(map(int, input().split())) for _ in range(N)]
adj = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        loc = locs[i]
        factory = factories[j]
        adj[i][j] = abs(loc[0] - factory[0]) + abs(loc[1] - factory[1])

all_factories = {k for k in range(N)}
minV = 400 * N
for i in range(N):
    DFS(0, adj[0][i], {i})
print(minV)
