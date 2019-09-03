import sys

sys.stdin = open('sample_input.txt', 'r')


def is_right_index_range(i, j):
    return 0 <= i < N and 0 <= j < N


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    board[N // 2][N // 2] = board[N // 2 - 1][N // 2 - 1] = 'W'
    board[N // 2 - 1][N // 2] = board[N // 2][N // 2 - 1] = 'B'

    for _ in range(M):
        j_, i_, player = map(int, input().split())

        # 1 흑돌
        # 2 백돌
        mine = 'B' if player == 1 else 'W'
        enemy = 'B' if mine == 'W' else 'W'

        # 인덱스 좌표계로 변경
        i = i_ - 1
        j = j_ - 1

        # 돌놓기
        board[i][j] = mine

        # 8군데 체크
        d = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for dx, dy in d:

            ni = i + dx
            nj = j + dy

            # 범위 안
            if is_right_index_range(ni, nj):
                # 적이 있는 방향일때
                if board[ni][nj] != mine and board[ni][nj] != 0:

                    enemy_locations = []

                    while True:
                        if not is_right_index_range(ni, nj) or board[ni][nj] == 0:  # 벽이거나 아무것도 없을때
                            break
                        elif board[ni][nj] == enemy:  # 적일때
                            enemy_locations.append([ni, nj])
                        elif board[ni][nj] == mine:  # 나를 다시 만났을때
                            # 만난 적들 다 뒤집기
                            for ex, ey in enemy_locations:
                                board[ex][ey] = mine
                            break

                        ni += dx
                        nj += dy
    count_w = 0
    count_b = 0
    for row in board:
        count_w += row.count('W')
        count_b += row.count('B')

    print("#{} {} {}".format(tc, count_b, count_w))
