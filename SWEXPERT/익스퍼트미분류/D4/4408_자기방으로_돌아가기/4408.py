import sys

sys.stdin = open('sample_input.txt', 'r')


def get_index(number):
    index = number // 2
    # 짝수면
    if number % 2 == 0:
        index -= 1

    return index


T = int(input())

for tc in range(1, T + 1):
    rooms = [0] * 200

    N = int(input())

    for _ in range(N):
        start, end = map(int, input().split())
        s_idx = get_index(start)
        e_idx = get_index(end)

        if s_idx > e_idx:
            s_idx, e_idx = e_idx, s_idx

        for i in range(s_idx, e_idx + 1):
            rooms[i] += 1

    print("#{} {}".format(tc, max(rooms)))
