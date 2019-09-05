import sys

sys.stdin = open('sample_input.txt', 'r')


class Atom:
    def __init__(self, x, y, direction, e):
        self.x = x
        self.y = y
        self.direction = direction
        self.e = e
        self.is_dead = False  # 터지면 True로 변경됨

    def move(self):

        if self.direction == 0:
            self.y += 0.5
        elif self.direction == 1:
            self.y -= 0.5
        elif self.direction == 2:
            self.x -= 0.5
        elif self.direction == 3:
            self.x += 0.5

        return self.x, self.y


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 받은 원자들 저장
    atoms = []
    for _ in range(N):
        x, y, direction, energy = map(int, input().split())
        atom = Atom(x, y, direction, energy)  # 원자 인스턴스 생성
        atoms.append(atom)

    total_energy = 0
    sec = 0
    while sec < 4000:
        sec += 0.5
        locations = {}

        for atom in atoms:
            if not atom.is_dead:
                coordinate = atom.move()
                if coordinate in locations:
                    locations[coordinate].append(atom)
                else:
                    locations[coordinate] = [atom]

        for coordinate in locations:
            if len(locations[coordinate]) >= 2:

                for atom in locations[coordinate]:
                    total_energy += atom.e
                    atom.is_dead = True

    print("#{} {}".format(tc, total_energy))
