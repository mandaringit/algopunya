def make_board(N):

    board = []
    for i in range(N):
        board.append([0] * N)

    std = N // 2

    board[std - 1][std - 1] = board[std][std] = "W"
    board[std][std - 1] = board[std - 1][std] = "B"

    return board


def isRightIndexRange(x, y, N):
    return 0 <= x <= N - 1 and 0 <= y <= N - 1


def isEnemy(x, y, enemy, board):
    return board[x][y] == enemy


def play_game(board, x, y, player, enemy):

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:

            around_x = x + i
            around_y = y + j

            if isRightIndexRange(around_x, around_y, N) and isEnemy(around_x, around_y, enemy, board):

                copy_x = x
                copy_y = y

                enemy_location = []

                while isRightIndexRange(copy_x + i, copy_y + j, N):

                    copy_x = copy_x + i
                    copy_y = copy_y + j

                    board_value = board[copy_x][copy_y]

                    if board_value == 0:
                        break

                    elif board_value != player:
                        enemy_location.append([copy_x, copy_y])

                    elif board_value == player:
                        for location in enemy_location:
                            board[location[0]][location[1]] = player
                        break

    return board


def count(board):
    white = 0
    black = 0
    for i in board:
        count_white = i.count("W")
        white += count_white
        count_black = i.count("B")
        black += count_black

    return white, black

# 실행


T = int(input())

for t in range(1, T + 1):
    N, M = (map(int, input().split()))

    board = make_board(N)

    for round in range(M):
        y, x, player = (map(int, input().split()))

        x = x - 1
        y = y - 1

        player = "B" if player == 1 else 'W'
        enemy = "B" if player == 'W' else 'W'

        board[x][y] = player

        board = play_game(board, x, y, player, enemy)

    white, black = count(board)

    print(f"#{t} {black} {white}")
