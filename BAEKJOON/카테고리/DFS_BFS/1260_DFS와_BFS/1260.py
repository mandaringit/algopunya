import sys

sys.stdin = open('input.txt', 'r')


def DFS(start, graph):
    stack = [start]

    visited = []

    while stack:
        node = stack.pop(-1)

        if node not in visited:

            visited.append(node)

            # 작은 순서대로 가기 위해서 정렬 -> 뒤집기가 필요함 (뒤에서 빼니까)
            childes = sorted(list(graph[node]))

            childes.reverse()

            for child in childes:

                if child not in visited:
                    stack.append(child)

    return visited


def BFS(start, graph):
    q = [start]

    visited = []

    while q:
        node = q.pop(0)

        if node not in visited:

            visited.append(node)

            # 작은 순서대로 가기 위해서 정렬이 필요함 (앞에서 빼니까)
            childes = sorted(list(graph[node]))

            for child in childes:

                if child not in visited:
                    q.append(child)
    return visited


N, M, V = map(int, input().split())

graph = {}

for i in range(1, N + 1):
    graph[i] = set()

for _ in range(M):
    node1, node2 = map(int, input().split())

    graph[node1].add(node2)
    graph[node2].add(node1)

print(" ".join(map(str, DFS(V, graph))))
print(" ".join(map(str, BFS(V, graph))))
