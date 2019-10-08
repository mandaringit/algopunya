import sys

sys.stdin = open('input.txt', 'r')

# 시간초과

def BFS(start, target):
    visited = [0] * 10000
    visited[start] = 1
    q = [(start, [])]

    while q:
        x, path = q.pop(0)

        for cmd in ['D', 'S', 'L', 'R']:
            if cmd == 'D':
                nx = 2 * x
                if nx >= 10000:
                    nx %= 10000

            elif cmd == 'S':
                nx = x - 1
                if nx < 0:
                    nx = 9999

            # L, R 변환을 좀 더 낫게끔...변환해야..
            elif cmd == 'L':
                str_x = list(str(x).zfill(4))
                str_x = str_x[1:] + [str_x[0]]
                nx = int(''.join(str_x))

            elif cmd == 'R':
                str_x = list(str(x).zfill(4))
                str_x = [str_x[3]] + str_x[:3]
                nx = int(''.join(str_x))

            if visited[nx] == 0:

                if nx == target:
                    return path + [cmd]
                else:
                    visited[nx] = 1
                    q.append((nx, path + [cmd]))


import timeit

s = timeit.default_timer()

T = int(input())

for tc in range(1, T + 1):
    start, target = map(int, input().split())

    print(''.join(BFS(start, target)))

e = timeit.default_timer()

print((e - s) * 1000)
