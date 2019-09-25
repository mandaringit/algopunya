import sys

sys.stdin = open('input.txt', 'r')

T = int(input())


def BFS(x, y):
    global space
    global limit
    q = [x]

    space[x] = 0

    while q:

        _x = q.pop(0)
        k = space[_x]

        for dx in [k - 1, k, k + 1]:

            nx = _x + dx

            if 0 <= nx < limit:

                if space[nx] == -1 or nx == y:
                    space[nx] = space[_x] + 1

                    if nx == y and dx == 1 :
                        return space[nx]
                    else:
                        q.append(nx)


for tc in range(1, T + 1):
    x, y = map(int, input().split())
    limit = y + 100
    space = [-1] * limit

    print(BFS(x, y))
