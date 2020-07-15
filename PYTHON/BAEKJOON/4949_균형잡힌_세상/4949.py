import sys

sys.stdin = open('input.txt', 'r')

while True:
    sentence = input()

    if sentence == '.':
        break

    stack = []

    result = 'yes'

    for char in sentence:
        if char == '(' or char == '[':
            stack.append(char)

        elif char == ']':
            if len(stack) == 0:
                result = 'no'
                break

            popped = stack.pop()

            if popped != '[':
                result = 'no'

        elif char == ')':
            if len(stack) == 0:
                result = 'no'
                break

            popped = stack.pop()

            if popped != '(':
                result = 'no'
                break

    if len(stack) != 0:
        result = 'no'

    print(result)
