import sys

sys.stdin = open('input.txt', 'r')

while True:
    numbers = list(map(int, input().split()))

    if numbers == [0, 0, 0]:
        break
    else:
        numbers.sort()
        x, y, z = numbers

        if x ** 2 + y ** 2 == z ** 2:
            print('right')
        else:
            print('wrong')