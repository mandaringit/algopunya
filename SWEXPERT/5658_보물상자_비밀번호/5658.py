import sys

sys.stdin = open('sample_input.txt', 'r')


class Node:

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self, N, iterable=None):
        self.head = None
        self.tail = None
        self.length = 0
        self.N = N // 4

        if iterable:
            for value in iterable:
                self.push(value)

    def push(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.length += 1

    def pop(self):

        if not self.head:
            return None
        else:
            node = self.tail
            prev_node = self.tail.prev
            prev_node.next = None
            self.tail = prev_node

            self.length -= 1

            node.prev = None

            return node

    def pushleft(self, value):

        if not self.head:
            self.push(value)

        else:
            node = Node(value)
            node.next = self.head
            self.head.prev = node
            self.head = node

            self.length += 1

    def rotate(self):
        value = self.pop().value
        self.pushleft(value)

    def values(self):
        hex_numbers = []

        current = self.head
        unit = []
        for i in range(self.length):
            unit.append(current.value)
            current = current.next

        for i in range(0, len(unit), self.N):
            hex_numbers.append(''.join(unit[i:i + self.N]))

        return hex_numbers


T = int(input())

for tc in range(1, T + 1):
    # N개의 숫자, 내림차순정렬 했을때 K번째 숫자를 구하자.
    N, K = map(int, input().split())

    numbers = list(input())

    DLL = DoublyLinkedList(N, numbers)

    possible_hex = set(DLL.values())
    for i in range(N // 4 - 1):
        DLL.rotate()
        possible_hex.update(DLL.values())

    possible_hex = sorted(list(map(lambda x: int(x, 16), possible_hex)), reverse=True)
    print("#{} {}".format(tc, possible_hex[K - 1]))
