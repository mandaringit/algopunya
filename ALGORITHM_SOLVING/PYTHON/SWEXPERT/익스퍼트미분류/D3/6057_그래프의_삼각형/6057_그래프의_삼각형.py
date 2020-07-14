# 아직 통과 못함
# 50개중 8개

import sys

sys.stdin = open('s_input.txt', 'r')


def BFS(S, graph):
    q = []

    q.append(S)

    visited = []
    d = {}

    d[S] = 0

    while q:
        std_node = q.pop(0)
        visited.append(std_node)

        for node in graph[std_node]:
            if node not in visited:
                q.append(node)
                if node not in d:
                    d[node] = d[std_node] + 1

    return d

    # 여기 노드들은 모두 std_node와 연결되어 있다. 즉 서로간의 연결을 살펴보면 된다.


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    graph = {i: [] for i in range(1, N + 1)}

    for m in range(1, M + 1):
        node1, node2 = map(int, input().split())

        graph[node1].append(node2)
        graph[node2].append(node1)

    print(BFS(1, graph))

    # print(f"#{t}")
