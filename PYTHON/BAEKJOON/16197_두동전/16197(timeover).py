import sys

sys.stdin = open('input.txt', 'r')

# 61 %  -> pop(0) 의 비효율성

class Coin:

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.is_fallen = False

    def move(self, direction):
        global board
        global N, M

        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        ni = self.i + d[direction][0]
        nj = self.j + d[direction][1]

        if 0 <= ni < N and 0 <= nj < M:
            if board[ni][nj] in ['o', '.']:
                self.i = ni
                self.j = nj
        else:
            self.is_fallen = True


def BFS(coins):
    global minCount
    start = (coins, 0)
    q = [start]

    while q:
        coins_, count = q.pop(0)

        coin1 = coins_[0]
        coin2 = coins_[1]

        for d in range(4):
            ncoin1 = Coin(coin1.i, coin1.j)
            ncoin2 = Coin(coin2.i, coin2.j)

            ncoin1.move(d)
            ncoin2.move(d)
            ncount = count + 1

            if ncount == 11:
                minCount = -1
                return

            elif (ncoin1.is_fallen, ncoin2.is_fallen) in [(True, False), (False, True)]:
                if ncount < minCount:
                    minCount = ncount
                    return

            elif (ncoin1.is_fallen, ncoin2.is_fallen) == (False, False):
                if (coin1.i, coin1.j) != (ncoin1.i, ncoin1.j) or (coin2.i, coin2.j) != (ncoin2.i, ncoin2.j):
                    ncoins = (ncoin1, ncoin2)
                    q.append((ncoins, ncount))

    if minCount == 11:
        minCount = -1


N, M = map(int, input().split())  # row , col
board = [list(input()) for _ in range(N)]

minCount = 11
coins = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coins.append(Coin(i, j))

BFS(coins)
print(minCount)
