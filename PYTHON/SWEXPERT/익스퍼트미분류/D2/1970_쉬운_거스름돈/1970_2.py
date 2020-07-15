import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    wons = {
        50000: 0,
        10000: 0,
        5000: 0,
        1000: 0,
        500: 0,
        100: 0,
        50: 0,
        10: 0
    }

    for won in wons.keys():
        count = N // won
        wons[won] += count

        N = N % won
        if N == 0:
            break

    print(f"#{tc}")
    print(" ".join(map(str, wons.values())))
