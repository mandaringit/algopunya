import sys

sys.stdin = open('input.txt', 'r')


def and_operator(number):
    N = 1
    while number > N * (N + 1) / 2:
        N += 1

    end_number = (N * (N + 1)) // 2
    gap = end_number - number

    return [N - gap, 1 + gap]


def add(loc1, loc2):
    return [loc1[0] + loc2[0], loc1[1] + loc2[1]]


def hash_operator(loc):
    p1, p2 = loc
    N = p1 + p2 - 1  # N 번째 대각선

    value = N * (N + 1) // 2
    gap = N - p1

    value -= gap
    return value


T = int(input())

for tc in range(1, T + 1):
    p1, p2 = map(int, input().split())

    hash_this = add(and_operator(p1), and_operator(p2))
    print("#{} {}".format(tc, hash_operator(hash_this)))
