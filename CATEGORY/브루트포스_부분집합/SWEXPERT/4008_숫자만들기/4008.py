# import sys
#
# sys.stdin = open('sample_input.txt', 'r')
#
#
# def perm(n, k):
#     global operators
#     global numbers
#
#     if n == k:
#
#         return
#     else:
#         for i in range(n, k):
#             operators[n], operators[i] = operators[i], operators[n]
#             perm(n + 1, k)
#             operators[n], operators[i] = operators[i], operators[n]
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     ops = list(map(int, input().split()))
#     numbers = list(map(int, input().split()))
#
#     operators = []
#     for i in range(4):
#         count = ops[i]
#         if count != 0:
#             if i == 0:
#                 operators += ['+'] * count
#             elif i == 1:
#                 operators += ['-'] * count
#             elif i == 2:
#                 operators += ['*'] * count
#             elif i == 3:
#                 operators += ['/'] * count
#
#     perm(0, sum(ops))
