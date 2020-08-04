import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):

    origin = input()

    now_bit = '0'

    count = 0

    for bit in origin:

        if now_bit != bit:
            count += 1

            now_bit = '0' if now_bit == '1' else '1'

    print("#{} {}".format(tc, count))
