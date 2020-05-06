# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    words = S.split(" ")
    stack = []

    for word in words:
        stack_length = len(stack)
        # 숫자면 푸시
        if word.isdigit():
            stack.append(int(word))
        elif word == "POP" and stack_length > 0:
            stack.pop()
        elif word == "DUP" and stack_length > 0:
            stack.append(stack[-1])
        elif word == "+" and stack_length > 1:
            topmost = stack.pop()
            second = stack.pop()
            stack.append(topmost + second)
        elif word == "-" and stack_length > 1:
            topmost = stack.pop()
            second = stack.pop()
            stack.append(topmost - second)
        else:
            return -1

    if len(stack) == 0:
        return -1

    return stack[-1]


print(solution("13 DUP 4 POP 5 DUP + DUP + -"))
print(solution("5 6 + -"))
print(solution("3 DUP 5 - -"))
