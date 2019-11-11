# 고민해보자...

import sys

sys.stdin = open('input.txt', 'r')


def calc_process(convert_stack):
    calc_stack = []

    try:

        while len(convert_stack) != 0:
            popped = convert_stack.pop()

            if popped == '*':
                num1 = calc_stack.pop()
                num2 = calc_stack.pop()
                popped = num1 * num2

            elif popped == '+':
                num1 = calc_stack.pop()
                num2 = calc_stack.pop()
                popped = num1 + num2

            calc_stack.append(popped)

    except:
        return None

    result = calc_stack[0]

    return result


def bracket_process(brackets):
    bracket_stack = []
    convert_stack = []

    bracket_stack.append(brackets[0])

    prev = brackets[0]

    total = 0

    for bracket in brackets[1:]:

        if len(bracket_stack) == 0:

            calc_result = calc_process(convert_stack)

            if calc_result:
                total += calc_result
            else:
                return 0

            convert_stack = []

            # 이후 푸시
            if bracket == '(' or bracket == '[':
                bracket_stack.append(bracket)
            else:
                return 0
        else:
            if bracket == '(' or bracket == '[':
                bracket_stack.append(bracket)

                if prev in ['(', '[']:
                    convert_stack.append('*')
                elif prev in [')', ']']:
                    convert_stack.append('+')
            else:
                popped = bracket_stack.pop()

                if popped == '(' and bracket == ')':
                    convert_stack.append(2)
                elif popped == '[' and bracket == ']':
                    convert_stack.append(3)
                else:
                    return 0

        prev = bracket

    if len(bracket_stack) != 0:
        return 0

    calc_result = calc_process(convert_stack)

    if calc_result:
        total += calc_result
    else:
        return 0

    return total


brackets = list(input())

print(bracket_process(brackets))
