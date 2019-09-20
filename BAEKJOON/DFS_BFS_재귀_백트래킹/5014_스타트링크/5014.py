import sys

sys.stdin = open('input.txt', 'r')


def BFS(start, goal):
    global building
    global U, D, F

    q = [start]
    building[start] = 0
    while q:

        x = q.pop(0)

        if x == goal:
            return building[x]
        else:
            d = (U, -D)
            for dx in d:
                nx = x + dx

                if 0 < nx <= F:
                    if building[nx] == -1:
                        building[nx] = building[x] + 1
                        if nx == goal:
                            return building[nx]
                        q.append(nx)

    return 'use the stairs'


# 전체 길이, 현재위치, 목적지, 올라갈수있는거리,내려갈수있는거리
F, S, G, U, D = map(int, input().split())

building = [-1] * (F + 1)

print(BFS(S, G))
