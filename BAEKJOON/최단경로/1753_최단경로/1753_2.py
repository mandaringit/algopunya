import sys

sys.stdin = open('input.txt', 'r')

# 시간초과

V, E = map(int, input().split())
K = int(input())  # 시작 정점

adj = {}
D = [11 * V for _ in range(V + 1)]
D[K] = 0

for _ in range(E):
    n1, n2, w = map(int, input().split())
    adj[(n1, n2)] = w

nodes = {i for i in range(1, V + 1)}
visited_nodes = {K}

for node in nodes - visited_nodes:
    weight = adj.get((K, node))
    if weight:
        if 0 < weight <= 10:
            D[node] = weight

while nodes != visited_nodes:
    minimum_node = None
    minW = 11 * V
    for node in nodes - visited_nodes:
        if D[node] <= minW:
            minimum_node = node
            minW = D[node]

    visited_nodes = visited_nodes | {minimum_node}

    for i in range(1, V + 1):
        w = adj.get((minimum_node, i))
        if w:
            if 0 < w <= 10:  # 인접하면
                D[i] = min(D[i], D[minimum_node] + w)

for i in range(1, V + 1):
    value = D[i]
    print(D[i]) if value != V * 11 else print('INF')
