import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    rooms = [0] + list(map(int, input().split()))

    basic_rooms = [0] * (N + 1)

    count = 0

    for i in range(1, N + 1):

        if basic_rooms[i] != rooms[i]:
            for j in range(i, N + 1, i):
                basic_rooms[j] = 0 if basic_rooms[j] else 1

            count += 1

        if basic_rooms == rooms:
            break

    print("#{} {}".format(tc, count))
