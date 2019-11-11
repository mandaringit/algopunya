import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    date = input()

    year = date[:4]
    month = date[4:6]
    day = date[6:]

    day_limit = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if 1 <= int(month) <= 12 and 1 <= int(day) <= day_limit[int(month)]:
        result = f"{year}/{month}/{day}"
    else:
        result = -1

    print(f"#{tc} {result}")
