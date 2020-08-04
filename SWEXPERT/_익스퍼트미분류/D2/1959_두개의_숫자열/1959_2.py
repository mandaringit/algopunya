import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):

    a_len, b_len = map(int, input().split())

    # 길이비교
    if a_len >= b_len:
        long = list(map(int, input().split()))
        short = list(map(int, input().split()))
    else:
        short = list(map(int, input().split()))
        long = list(map(int, input().split()))

    max_total = 0  # 모두다 음수일 수도 있다. 초깃값 설정에서 고민해야 할 수도 있다.
    for i in range(0, len(long) - len(short) + 1):
        pairs = zip(long[i:i + len(short)], short)

        total = 0
        for num1, num2 in pairs:
            total += num1 * num2

        if total > max_total:
            max_total = total

    print(f"#{tc} {max_total}")
