def I(x, y, s, codes):
    for i in range(y):
        codes.insert(x, s[i])

    return codes


def D(x, y, codes):
    codes = codes[:x] + codes[x + y:]
    return codes


for tc in range(1, 11):
    N = int(input())

    original_codes = list(map(int, input().split()))

    order_count = int(input())

    commands = input().split()

    for i, cmd in enumerate(commands):
        if cmd == 'I':
            s = []
            x = int(commands[i + 1])
            y = int(commands[i + 2])

            for j in range(y - 1, -1, -1):
                s.append(commands[i + 3 + j])

            I(x, y, s, original_codes)

        if cmd == 'D':
            x = int(commands[i + 1])
            y = int(commands[i + 2])

            D(x, y, original_codes)

        if cmd == 'A':
            y = int(commands[i + 1])
            for j in range(y):
                original_codes.append(commands[i + 2 + j])

    print(f"#{tc} {' '.join(original_codes[:10])}")
