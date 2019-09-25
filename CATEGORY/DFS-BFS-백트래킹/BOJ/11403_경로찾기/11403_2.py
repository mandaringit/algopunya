import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


def BFS(start, goal):
    global G
    global result

    visited = set()
    q = deque([start])

    while q:

        node = q.popleft()

        if node == goal and len(visited) > 0:  # 본인도 다시 돌아와서 만나야 True 라고 할수 있음
            result = True
            break
        else:

            for child in G[node] - visited:
                q.append(child)
                visited.add(child)


N = int(input())

# 그래프 만들기
G = {i: set() for i in range(N)}

for i in range(N):
    connection = list(map(int, input().split()))

    for j in range(len(connection)):
        if connection[j]:
            G[i].add(j)

arr = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        result = False
        BFS(i, j)

        if result:
            arr[i][j] = 1

for line in arr:
    print(' '.join(map(str, line)))
