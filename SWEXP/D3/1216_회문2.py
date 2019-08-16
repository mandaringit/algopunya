def check_palindrome_one_line(line, max_length, N):
    for i in range(0, N):
        f_char = line[i]

        for j in range(i + 1, N):
            b_char = line[j]

            if f_char == b_char:
                word = line[i:j + 1]
                if len(word) > max_length and word == word[::-1]:
                    max_length = len(word)

    return max_length


for tc in range(1, 11):
    tc_num = int(input())
    N = 100
    chars = [input() for _ in range(N)]

    max_length = 0

    # 가로 확인
    # 한줄씩 선택
    for row in chars:
        # 한줄에서
        max_length = check_palindrome_one_line(row, max_length, N)

    # 세로 확인
    for i in range(0, N):
        col = ''
        for j in range(0, N):
            col += chars[j][i]
        # 구한 col에서
        max_length = check_palindrome_one_line(col, max_length, N)

    print(f"#{tc} {max_length}")
