import sys

sys.stdin = open('sample_input.txt', 'r')


def validation(decoded_passwords):
    odd_sum = 0
    even_sum = 0
    for i in range(len(decoded_passwords)):
        # 여기선 홀수
        if i % 2 == 0:
            odd_sum += decoded_passwords[i]
        else:
            even_sum += decoded_passwords[i]

    result = odd_sum * 3 + even_sum

    if result // 10 == result / 10:
        return True
    else:
        return False


def decode(code):
    global template

    full_code = code[0]
    multiple = code[1]

    non_decoded_passwords = []

    code_unit = ''

    for char in full_code[::multiple]:
        code_unit += char
        if len(code_unit) == 7:
            non_decoded_passwords.append(code_unit)
            code_unit = ''

    decoded_passwords = []
    for unit in non_decoded_passwords:
        try:
            number = template[unit]
            decoded_passwords.append(number)
        except:
            pass

    if validation(decoded_passwords):
        return sum(decoded_passwords)
    else:
        return False


template = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    signals = set(input() for _ in range(N))

    # 16진수 암호 셋 구하기
    base2codes = set()
    for line in signals:
        if line != '0' * M:

            new_line = ''
            for char in line:
                binary = bin(int(char, 16)).replace('0b', '').zfill(4)
                new_line += binary

            strip_lines = new_line.rstrip('0')  # 1. 일단 처음으로 오른쪽을 친다.

            i = 0
            while len(strip_lines) > 0:
                i += 1
                pattern = strip_lines[-(7 * i):]  # 맨뒤에서부터 7*i 자리 수를 구한다
                multiple_pattern = pattern[::i]
                if multiple_pattern in template:  # 템플릿에 패턴에서 i씩 건너며 가져온 값이 패턴에 있는지 확인

                    all_password = strip_lines[-(56 * i):].zfill(56 * i)

                    base2codes.add((all_password, i))

                    strip_lines = strip_lines[: - (56 * i)].rstrip('0')  # 다음에 볼 라인은 처음부터 자른것 제외한라인
                    i = 0

    results = []
    for base2code in base2codes:
        ans = decode(base2code)
        if ans:
            results.append(ans)

    print("#{} {}".format(tc, sum(results)))
