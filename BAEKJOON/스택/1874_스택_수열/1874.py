# 시간을 더 줄일 수 있으면 좋긴 함

import sys

sys.stdin = open('input.txt', 'r')


def check_stack(n_list):
    stack = []

    push_this = 1

    result = []
    for need_this in n_list:

        if push_this <= need_this:

            for num in range(push_this, need_this + 1):
                stack.append(num)
                result.append('+')

            push_this = need_this + 1

        popping_number = stack.pop()

        if popping_number != need_this:
            return 'NO'

        result.append('-')

    return "\n".join(result)


N = int(input())

number_list = list(int(input()) for _ in range(N))

print(check_stack(number_list))
