import sys

sys.stdin = open('input.txt', 'r')


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:

    def __init__(self):
        self.front = None
        self.last = None

    def enqueue(self, value):
        node = Node(value)

        if not self.front:
            self.front = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

        return self

    def dequeue(self):

        if not self.front:
            return None
        else:
            node = self.front
            self.front = node.next

            return node


N, M = map(int, input().split())

numbers = [num for num in range(1, N + 1)]

all_seq = []

for i in range(N):
    q = Queue()
    q.enqueue([numbers[i]])

    while q.front:
        node = q.dequeue()

        if len(node.value) == M:
            all_seq.append(node.value)
        else:
            for num in numbers:
                new_seq = node.value + [num]
                q.enqueue(new_seq)

for seq in all_seq:
    print("{}".format(' '.join(map(str, seq))))
