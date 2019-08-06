def make_board(N):

    board = []
    for i in range(N):
        board.append([0] * N)

    std = N // 2

    board[std - 1][std - 1] = board[std][std] = "W"
    board[std][std - 1] = board[std - 1][std] = "B"

    return board


def play_game(board, x, y, player, enemy):

    for i in range(-1, 2):
        for j in range(-1, 2):

            around_x = x + i
            around_y = y + j

            if 0 <= around_x <= N - 1 and 0 <= around_y <= N - 1:

                if (around_x, around_y) != (
                        x, y) and board[around_x][around_y] == enemy:

                    new_x = x
                    new_y = y

                    # 조건하나 추가 19개 -> 26개
                    # 두칸 뛴게 범위 안이거나
                    if 0 <= new_x+(2*i) <= N-1 and 0 <= new_y+(2*j) <= N-1:

                        # 0 이 아닐때만
                        if board[new_x+(2*i)][new_y+(2*j)]:

                            change_this = []

                            while 0 <= new_x + i <= N - 1 and 0 <= new_y + j <= N - 1:

                                new_x = new_x + i
                                new_y = new_y + j

                                this_board_value = board[new_x][new_y]

                                if this_board_value != player:
                                    change_this.append([new_x, new_y])

                                if this_board_value == player:
                                    for c_arr in change_this:
                                        board[c_arr[0]][c_arr[1]] = player
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
