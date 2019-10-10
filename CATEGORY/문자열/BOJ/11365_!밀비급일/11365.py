import sys

sys.stdin = open('input.txt', 'r')

while True:
    code = input()

    if code == 'END':
        break

    print(code[::-1])
