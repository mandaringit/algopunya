import sys

sys.stdin = open('input.txt', 'r')

from collections import deque

dq = deque()

N = int(sys.stdin.readline())

for _ in range(N):

    cmds = sys.stdin.readline().split()

    cmd = cmds[0]

    if cmd == 'push_front':
        dq.appendleft(cmds[1])

    elif cmd == 'push_back':
        dq.append(cmds[1])

    elif cmd == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())

    elif cmd == 'pop_back':
        if len(dq) == 0:
            print(-1)

        else:
            print(dq.pop())
    elif cmd == 'size':
        print(len(dq))

    elif cmd == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)

    elif cmd == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif cmd == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
