import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


def BFS(x, y):
    global relation

    q = deque()
    q.append([x, set()])

    while q:
        people, path = q.popleft()

        if people == y:
            return len(path)
        else:

            for node in relation[people] - path:
                if node == y:
                    return len(path | {node})
                else:
                    q.append([node, path | {node}])

    return -1


N = int(input())

p1, p2 = map(int, input().split())

M = int(input())

relation = {}

for _ in range(M):
    parent, child = map(int, input().split())

    # 촌수는 양방향
    if parent in relation:
        relation[parent].add(child)
    else:
        relation[parent] = {child}

    if child in relation:
        relation[child].add(parent)
    else:
        relation[child] = {parent}

print(BFS(p1, p2))
