import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


def BFS(N, K):
    q = deque()

    q.append(N)
    location = [0] * 100001

    while q:
        x = q.popleft()

        if x == K:
            return location[x]

        for next_x in [x + 1, x - 1, x * 2]:

            if 0 <= next_x <= 100000:
                if location[next_x] == 0:
                    q.append(next_x)
                    location[next_x] = location[x] + 1

    return None


N, K = map(int, input().split())

print(BFS(N, K))
