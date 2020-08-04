import sys

sys.stdin = open('input.txt', 'r')

# 끝나는 인덱스를 손으로 써보고 (미리 정해놓고) 짜보는게 좋다.

T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())

    numbers = list(map(int, input().split()))

    max_sum = 0
    min_sum = 10000 * N

    # 고정된 부분
    # 0 -> N - M
    for i in range(0, N - M + 1):

        total = 0

        # 움직이는 부분
        # 0 -> M - 1
        for j in range(i, i + M):
            total += numbers[j]

        if total > max_sum:
            max_sum = total

        if total < min_sum:
            min_sum = total

    print(f"#{tc} {max_sum - min_sum}")

