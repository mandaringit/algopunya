import sys

sys.stdin = open('input.txt','r')

def check_bracket(brackets):
    stack = []

    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return 'NO'

    if len(stack) > 0:
        return 'NO'

    return 'YES'


T = int(input())

for tc in range(1,T+1):

    brackets = list(input())

    print(check_bracket(brackets))

