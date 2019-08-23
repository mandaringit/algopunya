# readline으로 안읽으면 시간초과남

import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

stack = []

for _ in range(N):
    cmds = sys.stdin.readline().split()
    cmd = cmds[0]

    if cmd == 'push':
        stack.append(int(cmds[1]))
    elif cmd == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        print(1) if len(stack) == 0 else print(0)
    elif cmd == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
