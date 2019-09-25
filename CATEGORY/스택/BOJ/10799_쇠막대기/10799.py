import sys

sys.stdin = open('input.txt', 'r')

brackets = list(input())

pipe_count = 0

stack = [brackets[0]]

prev = brackets[0]

for bracket in brackets[1:]:

    if bracket == '(':
        stack.append(bracket)

    else:
        stack.pop()

        # 레이저 일때
        if prev == '(':
            pipe_count += len(stack)
        # 레이저가 아닌 쇠막대기의 끝일때
        else:
            pipe_count += 1

    prev = bracket

print(pipe_count)
