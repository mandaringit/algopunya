def move_left_right(board, N, direction):
    new_board = []

    for row in board:

        if direction == 'right':
            row.reverse()

        row = list(filter(lambda x: x != 0, row))

        length = len(row)

        i = 0
        merge_count = N - length
        new_line = []

        while i < length:
            # 맨 마지막이 시작 부분일 경우
            if i == length - 1:
                new_line.append(row[i])
                break
            else:
                part = row[i:i + 2]
                left = part[0]
                right = part[1]
                if left == right:
                    new_line.append(left + right)
                    merge_count += 1
                    i += 2
                else:
                    new_line.append(left)
                    if i == length - 2:
                        new_line.append(right)
                        break
                    i += 1

        for _ in range(merge_count):
            new_line.append(0)

        if direction == 'right':
            new_line.reverse()

        new_board.append(new_line)

    return new_board


def move_down_up(board, N, direction):
    new_board = [[] * N for _ in range(N)]

    board = list(zip(*board))

    for row in board:

        if direction == 'down':
            row = list(row)
            row.reverse()

        row = list(filter(lambda x: x != 0, row))

        length = len(row)

        i = 0
        merge_count = N - length
        new_line = []

        while i < length:
            # 맨 마지막이 시작 부분일 경우
            if i == length - 1:
                new_line.append(row[i])
                break
            else:
                part = row[i:i + 2]
                left = part[0]
                right = part[1]
                if left == right:
                    new_line.append(left + right)
                    merge_count += 1
                    i += 2
                else:
                    new_line.append(left)
                    if i == length - 2:
                        new_line.append(right)
                        break
                    i += 1

        for _ in range(merge_count):
            new_line.append(0)

        if direction == 'down':
            new_line.reverse()

        for i in range(N):
            new_board[i].append(new_line[i])

    return new_board


T = int(input())

for tc in range(1, T + 1):
    N, d = input().split()
    N = int(N)

    board = [list(map(int, input().split())) for _ in range(N)]

    if d == 'left' or d == 'right':
        new_board = move_left_right(board, N, d)
    else:
        new_board = move_down_up(board, N, d)

    print("#{}".format(tc))
    for row in new_board:
        print(' '.join(map(str, row)))
