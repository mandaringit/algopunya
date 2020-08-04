import sys

sys.stdin = open('sample_input.txt', 'r')


def DFS(i, j, total):
    global board
    global N
    global minV

    if [i, j] == [N - 1, N - 1]:
        if total < minV:
            minV = total
    else:
        if total < minV:
            d = [(1, 0), (0, 1)]

            for dx, dy in d:
                ni = i + dx
                nj = j + dy

                if 0 <= ni < N and 0 <= nj < N:
                    DFS(ni, nj, total + board[ni][nj])


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]
    minV = 10 * (2 * N - 1)

    DFS(0, 0, board[0][0])

    print("#{} {}".format(tc, minV))
