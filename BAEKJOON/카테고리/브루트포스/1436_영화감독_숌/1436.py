import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

hell_numbers = []

hell_number = 666
i = 0

while i != N:
    if '666' in str(hell_number):
        i += 1
        hell_numbers.append(hell_number)

    hell_number += 1

print(hell_numbers[N-1])
