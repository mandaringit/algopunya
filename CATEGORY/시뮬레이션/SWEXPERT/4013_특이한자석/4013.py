import sys

sys.stdin = open('sample_input.txt', 'r')


class Magnet:

    def __init__(self, mgs):
        self.magnets = mgs
        self.next_magnets = []
        self.left = None
        self.right = None

    def check(self, direction):
        self.check_left(direction)
        self.check_right(direction)
        self.rotate(direction)

    def check_left(self, direction):
        d = 1 if direction == -1 else -1

        if self.left:
            left_value = self.left.magnets[2]
            if self.magnets[6] != left_value:
                # rotate -> direction 반대로
                self.left.rotate(d)
                self.left.check_left(d)

    def check_right(self, direction):

        d = 1 if direction == -1 else -1

        if self.right:
            right_value = self.right.magnets[6]
            if self.magnets[2] != right_value:
                # rotate -> direction 반대로
                self.right.rotate(d)
                self.right.check_right(d)

    def rotate(self, direction):

        if direction == 1:  # 시계방향
            self.next_magnets = self.magnets[:]
            last = self.next_magnets.pop()
            self.next_magnets.insert(0, last)

        elif direction == -1:  # 반시계방향
            self.next_magnets = self.magnets[:]
            first = self.next_magnets.pop(0)
            self.next_magnets.append(first)

    def done(self):
        if self.next_magnets:
            self.magnets = self.next_magnets[:]


T = int(input())

for tc in range(1, T + 1):

    K = int(input())
    mgs = [0] * 4
    for i in range(4):
        poles = list(map(int, input().split()))
        mg = Magnet(poles)
        mgs[i] = mg

    for i in range(4):
        if i - 1 >= 0:
            mgs[i].left = mgs[i - 1]
        if i + 1 < 4:
            mgs[i].right = mgs[i + 1]

    # 회전
    for _ in range(K):
        num, direction = map(int, input().split())
        mgs[num - 1].check(direction)

        for magnet in mgs:
            magnet.done()

    total = 0
    for i in range(4):
        mg_value = mgs[i].magnets[0]
        if i == 0 and mg_value == 1:
            total += 1
        elif i == 1 and mg_value == 1:
            total += 2
        elif i == 2 and mg_value == 1:
            total += 4
        elif i == 3 and mg_value == 1:
            total += 8

    print("#{} {}".format(tc, total))
