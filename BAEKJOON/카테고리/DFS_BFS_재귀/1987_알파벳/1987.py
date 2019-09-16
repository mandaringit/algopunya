import sys

sys.stdin = open('input.txt', 'r')

# 메모리 초과

from collections import deque


def BFS(i, j):
    global board
    global R
    global C
    global maxV

    q = deque()
    q.append([i, j, [board[i][j]]])

    while q:
        i_, j_, path = q.popleft()

        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in d:
            ni = i_ + dx
            nj = j_ + dy

            if 0 <= ni < R and 0 <= nj < C:
                alphabet = board[ni][nj]
                if alphabet not in path:
                    next_path = path + [alphabet]
                    path_length = len(next_path)
                    if path_length > maxV:
                        maxV = path_length
                    q.append([ni, nj, next_path])


R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]
maxV = 0

BFS(0, 0)

print(maxV)
