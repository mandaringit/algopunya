import sys

sys.stdin = open('input.txt', 'r')


def BFS():
    global graph

    visited = [0] * 100
    visited[0] = 1
    stack = [0]

    while stack:
        node = stack.pop()

        for n in graph[node]:
            if n == 99:
                return 1
            else:
                if visited[n] == 0:
                    visited[n] = 1
                    stack.append(n)

    return 0


for _ in range(10):
    tc, E = map(int, input().split())
    edges = list(map(int, input().split()))
    graph = {i: set() for i in range(100)}

    for i in range(E):
        n1 = edges[2 * i]
        n2 = edges[2 * i + 1]
        graph[n1].add(n2)

    print("#{} {}".format(tc, BFS()))
