import sys

sys.stdin = open('input.txt', 'r')


def check():
    global brackets

    stack = [brackets[0]]
    for i in range(1, N):
        next_bracket = brackets[i]
        if next_bracket in ['(', '[', '{', '<']:
            stack.append(next_bracket)
        else:
            if not stack:
                return 0
            else:
                prev_bracket = stack[-1]
                if next_bracket == '}' and prev_bracket == '{':
                    stack.pop()
                elif next_bracket == ')' and prev_bracket == '(':
                    stack.pop()
                elif next_bracket == '>' and prev_bracket == '<':
                    stack.pop()
                elif next_bracket == ']' and prev_bracket == '[':
                    stack.pop()
                else:
                    return 0

    if len(stack) >= 1:
        return 0
    else:
        return 1


for tc in range(1, 11):
    N = int(input())
    brackets = list(input())

    print("#{} {}".format(tc, check()))