import sys

sys.stdin = open('input.txt', 'r')

# 시간 초과

def prim(start):
    global graph
    global max_weight

    possible_nodes = set(graph.keys())
    visited_nodes = {start}
    total_weight = 0

    while possible_nodes - visited_nodes:

        min_weight = max_weight
        min_node = None

        for node in visited_nodes:
            for child in graph[node] - visited_nodes:
                weight = adj[(node, child)]

                if weight < min_weight:
                    min_weight = weight
                    min_node = child

        total_weight += min_weight
        visited_nodes.add(min_node)

    return total_weight


V, E = map(int, input().split())

graph = {i: set() for i in range(1, V + 1)}
adj = {}

max_weight = 0
for _ in range(E):
    node1, node2, weight = map(int, input().split())

    if weight > max_weight:
        max_weight = weight

    graph[node1].add(node2)
    graph[node2].add(node1)

    adj[(node1, node2)] = weight
    adj[(node2, node1)] = weight

print(prim(1))
