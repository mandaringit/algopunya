import sys

sys.stdin = open('input.txt', 'r')


def Dijkstra(G, r):  # 그래프, 시작점
    global V, E, K, adj

    S = set()
    V_all = set(G.keys())
    d = [11] * (V + 1)
    d[r] = 0

    while S != V_all:
        # 아직 트리에 포함 안한 놈들 중 d가 가장 작은걸 꺼낸다.
        minD = 10000
        u = 0
        for i in V_all - S:
            if d[i] < minD:
                minD = d[i]
                u = i

        S = S | {u}

        for v in G[u]:
            # 방문 안했고, u의 최단값 + u->v로의 최단값의 합이 현재 v의 최단값보다 짧으면
            if v in V_all - S and d[u] + adj[(u, v)] < d[v]:
                d[v] = d[u] + adj[(u, v)]

    return d


V, E = map(int, input().split())  # 노드, 간선수
K = int(input())  # 시작 정점

G = {i: set() for i in range(1, V + 1)}
adj = {}

for _ in range(E):
    n1, n2, w = map(int, input().split())
    G[n1].add(n2)
    adj[(n1, n2)] = w

d = Dijkstra(G, K)
for i in range(1, V + 1):
    if d[i] == 11:
        print('INF')
    else:
        print(d[i])
