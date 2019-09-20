import sys

sys.stdin = open('input.txt', 'r')

# 연결요소는, 전부 연결해 봤을대 각각 독립적인 그래프의 개수 ?
# 시간 초과

from collections import deque


def BFS(start):
    global graph

    visited = set()

    q = deque()
    q.append(start)

    while q:

        node = q.popleft()

        for child in graph[node] - visited:
            q.append(child)
            visited.add(child)

    return visited


N, M = map(int, input().split())

graph = {i: set() for i in range(1, N + 1)}

for _ in range(M):
    node1, node2 = map(int, input().split())
    # 방향 없는 그래프
    graph[node1].add(node2)
    graph[node2].add(node1)

nodes = set(graph.keys())
total_visited = set()
count = 0

while total_visited != nodes:
    total_visited = total_visited | BFS(list(nodes - total_visited)[0])
    count += 1

print(count)
