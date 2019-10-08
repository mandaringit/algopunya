import sys

sys.stdin = open('input.txt', 'r')


# 아무대나 일단 가고 -> 거기서 다시 시작해서 또 가고 -> 그렇게 최대가 나올때 까지 계속

def BFS(start):
    global N

    q = [(start, 0)]
    visited = {start}
    maxV = 0
    max_node = None
    while q:
        x, cost = q.pop(0)

        for node in graph[x] - visited:
            visited.add(node)
            w = adj[(x, node)]
            q.append((node, cost + w))

            if w + cost > maxV:
                maxV = w + cost
                max_node = node

    return maxV, max_node


N = int(input())

adj = {}
graph = {i: set() for i in range(1, N + 1)}
for _ in range(N - 1):
    n1, n2, w = map(int, input().split())
    adj[(n1, n2)] = w
    adj[(n2, n1)] = w
    graph[n1].add(n2)
    graph[n2].add(n1)

maxV = 0
max_node = 1

while True:
    value, node = BFS(max_node)

    if value > maxV:
        max_node = node
        maxV = value
    else:
        break

print(maxV)
