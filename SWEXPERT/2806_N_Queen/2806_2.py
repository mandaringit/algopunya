# import sys
#
# sys.stdin = open('sample_input.txt', 'r')
#
#
# def is_ok(x, y, N):
#
#     return arounds
#
#
# class Node:
#
#     def __init__(self, x, y, depth, N):
#         self.x = x
#         self.y = y
#         self.depth = depth
#         self.board = [(self.x, self.y)]
#
#
# def DFS_BFS(start, N):
#     stack = [start]
#     count = 0
#     while stack:
#         node = stack.pop()
#
#         i = node.x + 1
#
#         if node.depth == N - 1:
#             count += 1
#         else:
#             # 밑에줄만 검사
#             for j in range(N):
#                 if (i, j) not in node.forbidden:
#                     next_node = Node(i, j, node.depth + 1, N)
#                     next_node.forbidden.update(node.forbidden)
#                     stack.append(next_node)
#
#     return count
#
#
# import timeit
#
# start1 = timeit.default_timer()
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#
#     count = 0
#
#     for j in range(N):
#         start = Node(0, j, 0, N)
#
#         count += DFS_BFS(start, N)
#     print("#{} {}".format(tc, count))
#
# end = timeit.default_timer()
#
# print(end - start1)
