import sys

sys.stdin = open('input.txt', 'r')


def DFS(start, N):
    stack = [start]

    state = []

    while stack:

        x, y = stack.pop()

        i = x + 1

        # 밑에줄만 검사
        for j in range(N):
            if


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    for j in range(N):
        start = [0, j]

        DFS(start, N)
