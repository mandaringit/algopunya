import sys

sys.stdin = open('sample_input.txt', 'r')


class Magnet:
    def __init__(self, blades):
        self.blades = blades
        self.left = None
        self.right = None
        self.is_rotated = [False, 0]

    def rotate(self):
        d = self.is_rotated[1]
        if d == 1:
            blade = self.blades.pop()
            self.blades.insert(0, blade)
        elif d == -1:
            blade = self.blades.pop(0)
            self.blades.append(blade)
        self.is_rotated = [False, 0]

    def check_left(self, d):
        self.is_rotated = [True, d]
        if self.left:
            if self.blades[6] != self.left.blades[2]:
                self.left.check_left(-d)

    def check_right(self, d):
        self.is_rotated = [True, d]
        if self.right:
            if self.blades[2] != self.right.blades[6]:
                self.right.check_right(-d)


T = int(input())
for tc in range(1, T+1):
    K = int(input())

    magnets = []
    for _ in range(4):
        blades = list(map(int, input().split()))
        magnet = Magnet(blades)
        magnets.append(magnet)

    for i in range(4):
        if 0 < i < 3:
            magnets[i].left = magnets[i-1]
            magnets[i].right = magnets[i+1]
        elif i == 0:
            magnets[i].right = magnets[i+1]
        elif i == 3:
            magnets[i].left = magnets[i-1]

    for _ in range(K):
        num, d = map(int, input().split())
        magnets[num-1].check_left(d)
        magnets[num-1].check_right(d)

        for magnet in magnets:
            if magnet.is_rotated[0]:
                magnet.rotate()

    total = 0
    scores = [1, 2, 4, 8]
    for idx, magnet in enumerate(magnets):
        value = magnet.blades[0]
        if value: total += scores[idx]

    print("#{} {}".format(tc, total))
