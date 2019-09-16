import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = float(input())

    binary = ''

    while N != 0:

        if len(binary) >= 13:
            binary = 'overflow'
            break

        N = N * 2
        int_part = int(N)

        if int_part == 1:
            binary += '1'
            N -= 1
        else:
            binary += '0'

    print("#{} {}".format(tc, binary))
