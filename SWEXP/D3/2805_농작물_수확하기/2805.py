import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    half = N // 2
    total = 0
    count = 0
    for _ in range(N):
        row = input()

        start_idx = 0 + half
        end_idx = N - half
        for i in range(start_idx, end_idx):
            this_number = row[i]
            total += int(row[i])
        count += 1
        if count > N // 2:
            half += 1
        else:
            half -= 1

    print(f"#{tc} {total}")
