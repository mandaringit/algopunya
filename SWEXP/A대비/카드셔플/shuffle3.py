import sys

sys.stdin = open('sample_input.txt', 'r')


class Node:

    def __init__(self, value, depth):
        self.value = value
        self.depth = depth
        self.next = None


class Queue:

    def __init__(self, node=None):
        self.first = None
        self.last = None
        self.size = 0

        if node:
            value, depth = node
            self.enqueue(value, depth)

    def enqueue(self, value, depth):
        new_node = Node(value, depth)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.size += 1

        return self

    def dequeue(self):
        if not self.first:
            return None
        else:
            temp = self.first

            if self.first == self.last:
                self.first = None
                self.last = None
            else:
                self.first = self.first.next

            self.size -= 1

            return temp


def shuffle(x, cards, N):
    half = N // 2
    left = cards[:half]
    right = cards[half:]

    if x < N // 2:
        l = left[:half - x]
        r = right[x:]
        middle = list(zip(right[:x], left[half - x:half]))

        shuffled = [*l]

        for i, j in middle:
            shuffled.append(i)
            shuffled.append(j)

        shuffled += r

        return shuffled

    else:
        x = N - 1 - x
        l = right[:half - x]
        r = left[x:]
        middle = list(zip(left[:x], right[half - x:half]))

        shuffled = [*l]

        for i, j in middle:
            shuffled.append(i)
            shuffled.append(j)

        shuffled += r

        return shuffled


def BFS(start, N):
    asc = sorted(start)
    dec = list(reversed(asc))
    q = Queue([start, 0])

    while q.size != 0:
        node = q.dequeue()

        cards = node.value
        depth = node.depth

        if depth > 5:
            return -1

        if cards == asc or cards == dec:
            return depth

        for i in range(1, N):
            shuffled = shuffle(i, cards, N)
            n_depth = depth + 1

            if shuffled == asc or shuffled == dec:
                return n_depth

            if n_depth < 5:
                q.enqueue(shuffled, n_depth)

    return -1


import timeit

start = timeit.default_timer()

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    cards = list(map(int, input().split()))

    print("#{} {}".format(tc, BFS(cards, N)))

end = timeit.default_timer()

print(end - start)
