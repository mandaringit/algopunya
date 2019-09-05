import sys

sys.stdin = open('input.txt', 'r')


def BFS(start, graph):
    q = [start]

    visited = []

    while q:

        node = q.pop(0)

        if node not in visited:
            visited.append(node)

            for child in graph[node]:
                if child not in visited:
                    q.append(child)

    return visited


N = int(input())

networks = {}

for i in range(1, N + 1):
    networks[i] = set()

connect_number = int(input())

for _ in range(connect_number):
    node1, node2 = map(int, input().split())

    networks[node1].add(node2)
    networks[node2].add(node1)

# 1번 컴퓨터로 인해 바이러스에 걸린 컴퓨터 = 방문길이 - 1 (1번은 빼야하니까)
print(len(BFS(1, networks)) - 1)
