import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    carrots = [0] + list(map(int, input().split()))
    border = 0
    min_diff = sum(carrots)
    for i in range(2, N - 1):
        area1 = sum(carrots[:i])
        area2 = sum(carrots[i:])

        diff = area1 - area2
        if diff < 0:
            diff = -diff
        if diff < min_diff:
            border = i - 1
            min_diff = diff

    print(f"#{tc} {border} {min_diff}")

