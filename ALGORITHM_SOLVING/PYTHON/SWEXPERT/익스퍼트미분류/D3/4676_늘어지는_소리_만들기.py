T = int(input())

for tc in range(1, T + 1):
    chars = list(input())
    hyphen = int(input())
    locations = list(map(int, input().split()))

    for i in locations:
        if i == 0:
            chars[0] = '-' + chars[0]
        else:
            idx = i - 1
            chars[idx] += '-'

    print(f"#{tc} {''.join(chars)}")
