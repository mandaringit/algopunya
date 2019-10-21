import sys

sys.stdin = open('input.txt', 'r')


# 기어는 4개 뿐이다. 충분히 다 가면서 돌려도 가능하다.
# 시작 톱니에서 처음에 자신을 돌리고 돌린 정보를 따로 저장(next_teeth)
# 왼쪽, 오른쪽을 나눠 체크 -> 각각의 톱니를 체크하고 돌려야 하는 톱니면 이전 방향의 역방향으로 돌리고 정보 저장,
# 모든 회전이 완료되면 마지막으로 현재 톱니랑 변화한 톱니가 서로 다른 경우, 현재 톱니를 변화한 톱니로 변경.

class Gear:
    def __init__(self, teeth):
        self.teeth = teeth
        self.left = None
        self.right = None
        self.next_teeth = []

    def rotate(self, d):
        if d == 1:
            self.next_teeth = self.teeth[:]
            last = self.next_teeth.pop()
            self.next_teeth = [last] + self.next_teeth
        else:
            self.next_teeth = self.teeth[:]
            first = self.next_teeth.pop(0)
            self.next_teeth = self.next_teeth + [first]

    def check_left(self, d):
        if self.left:
            if self.teeth[6] != self.left.teeth[2]:
                nd = -1 if d == 1 else 1
                self.left.rotate(nd)
                self.left.check_left(nd)

    def check_right(self, d):
        if self.right:
            if self.teeth[2] != self.right.teeth[6]:
                nd = -1 if d == 1 else 1
                self.right.rotate(nd)
                self.right.check_right(nd)

    def check(self, d):
        global gears

        self.rotate(d)
        self.check_left(d)
        self.check_right(d)

        for gear in gears:
            if gear.next_teeth != [] and gear.next_teeth != gear.teeth:
                gear.teeth = gear.next_teeth


# 톱니 생성
gears = [0, 0, 0, 0]
for i in range(4):
    teeth = list(map(int, input()))
    gears[i] = Gear(teeth=teeth)

# 짝 맞춰주기
gears[0].right = gears[1]
gears[1].left = gears[0]
gears[1].right = gears[2]
gears[2].left = gears[1]
gears[2].right = gears[3]
gears[3].left = gears[2]

# 회전
K = int(input())
for _ in range(K):
    idx, d = map(int, input().split())
    gears[idx - 1].check(d)

score = 0
for i, gear in enumerate(gears):
    if gear.teeth[0] == 1:
        if i == 0:
            score += 1
        elif i == 1:
            score += 2
        elif i == 2:
            score += 4
        elif i == 3:
            score += 8
print(score)
