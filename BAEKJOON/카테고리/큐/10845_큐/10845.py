import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())

q = []
for _ in range(N):

    cmds = list(sys.stdin.readline().split())
    cmd = cmds[0]
    if cmd == 'push':
        q.append(int(cmds[1]))

    elif cmd == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop(0))

    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif cmd == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
