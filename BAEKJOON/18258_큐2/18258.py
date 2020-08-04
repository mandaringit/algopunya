import sys


class Queue:
    def __init__(self, N):
        self.front = 0
        self.rear = 0
        self.queue = [0 for i in range(N)]

    def push(self, x):
        self.queue[self.rear] = x
        self.rear += 1

    def pop(self):
        if self.empty():
            return -1
        else:
            x = self.queue[self.front]
            self.front += 1
            return x

    def size(self):
        return self.rear - self.front

    def empty(self):
        return 1 if self.rear == self.front else 0

    def get_front(self):
        if self.empty():
            return -1
        else:
            return self.queue[self.front]

    def get_back(self):
        if self.empty():
            return -1
        else:
            return self.queue[self.rear-1]


input = sys.stdin.readline
N = int(input().rstrip('\n'))
queue = Queue(N)

for _ in range(N):
    cmd = input().rstrip('\n').split(' ')
    if cmd[0] == 'push':
        queue.push(int(cmd[1]))
    elif cmd[0] == 'pop':
        print(queue.pop())
    elif cmd[0] == 'front':
        print(queue.get_front())
    elif cmd[0] == 'back':
        print(queue.get_back())
    elif cmd[0] == 'size':
        print(queue.size())
    elif cmd[0] == 'empty':
        print(queue.empty())