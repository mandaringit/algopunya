import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


def process(dq, funcs):
    direction = 'left'

    for func in funcs:
        if func == 'R':
            direction = 'right' if direction == 'left' else 'left'

        elif func == 'D':
            if direction == 'left' and len(dq) != 0:
                dq.popleft()
            elif direction == 'right' and len(dq) != 0:
                dq.pop()
            else:
                return 'error'

    if direction == 'left':
        return str(list(dq)).replace(' ', '')
    else:
        return str(list(dq)[::-1]).replace(' ', '')


T = int(input())

for tc in range(1, T + 1):
    funcs = list(input())

    n = int(input())
    str_arr = input()
    str_arr = str_arr.replace('[', '')
    str_arr = str_arr.replace(']', '')

    dq = deque([int(char) for char in str_arr.split(',') if char.isdigit()])

    print(process(dq, funcs))
