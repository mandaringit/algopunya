import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    data = input().split()

    total_binary = ''

    for char in data[1]:
        binary = bin(int(char, 16)).replace('0b', '')
        total_binary += binary.zfill(4)

    print("#{} {}".format(tc, total_binary))
