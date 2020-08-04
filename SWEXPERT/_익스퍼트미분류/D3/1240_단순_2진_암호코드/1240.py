import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    information = [input() for _ in range(N)]

    keys = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }

    code_line = ''
    for row in information:
        if '1' in row:
            code_line = row
            break

    code_line = code_line.strip('0')
    code_line = code_line.zfill(56)

    codes = []
    for i in range(8):
        codes.append(code_line[i * 7:i * 7 + 7])

    decoded_number = ''
    for code in codes:
        decoded_number += str(keys[code])

    odd_sum = 0
    even_sum = 0
    validate_code = decoded_number[-1]
    for i in range(8):
        # 여기선 홀수임
        if i % 2 == 0:
            odd_sum += int(decoded_number[i])
        else:
            even_sum += int(decoded_number[i])

    total = odd_sum * 3 + even_sum

    result = 0
    if total / 10 == total // 10:
        for str_digit in decoded_number:
            result += int(str_digit)

    print("#{} {}".format(tc, result))
