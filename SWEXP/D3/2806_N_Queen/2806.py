import sys

sys.stdin = open('sample_input.txt', 'r')


def get_around(x, y, N):
    arounds = []

    d = [[-1, -1, False], [-1, 1, False], [1, -1, False], [1, 1, False], [1, 0, False], [0, 1, False],
         [-1, 0, False], [0, -1, False]]

    mul = 1
    is_all_true = 0

    while is_all_true != 8:

        for i in range(0, len(d)):

            dx, dy, stop = d[i]

            if not stop:
                if 0 <= x + dx * mul < N and 0 <= y + dy * mul < N:
                    arounds.append([x + dx * mul, y + dy * mul])
                else:
                    d[i][2] = True

        true_sum = 0
        for _, __, stop in d:
            if stop:
                true_sum += 1

        is_all_true = true_sum

        mul += 1

    return arounds


class Node:

    def __init__(self, x, y, depth, N):
        self.x = x
        self.y = y
        self.depth = depth
        self.forbidden = [[self.x, self.y]]


def DFS(start, N):
    stack = [start]

    while stack:
        node = stack.pop()

        node.forbidden.extend(get_around(node.x, node.y, N))

        i = node.x + 1

        # 밑에줄만 검사
        for j in range(N):
            if [i, j] not in node.forbidden:
                next_node = Node(i, j, node.depth + 1, N)
                next_node.forbidden.extend(node.forbidden)
                stack.append(next_node)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    for j in range(N):
        start = Node(0, j, 0, N)

        DFS(start, N)
