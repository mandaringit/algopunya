def check_board_one_line(line, board_len, word_len):
    count = 0
    for i in range(0, board_len - word_len + 1):
        first_char = line[i]  # 단어 첫글자
        last_char = line[i + word_len - 1]  # 단어 마지막 글자
        word = line[i:i + word_len]

        if first_char == last_char and word == word[::-1]:
            count += 1
    return count


for tc in range(1, 11):
    board_length = 8
    word_length = int(input())

    board = [input() for _ in range(board_length)]

    # 가로
    total_count = 0
    for row in board:
        total_count += check_board_one_line(row, board_length, word_length)

    # 세로
    col_board = list(zip(*board))
    for col in col_board:
        total_count += check_board_one_line(col, board_length, word_length)

    print(f"#{tc}", total_count)
