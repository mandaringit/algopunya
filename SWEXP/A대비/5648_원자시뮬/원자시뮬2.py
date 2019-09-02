import sys
# 이제 마지막으로, 각 방향이 서로를 가리키고 있는지 확인해야한다. ==> 추가해야함

sys.stdin = open('sample_input.txt', 'r')


class Atom:
    bomb = {}

    def __init__(self, x, y, direction, e):
        self.x = x
        self.y = y
        self.direction = direction
        self.e = e
        self.is_dead = False

    def compare(self, atom):

        if atom.direction == self.direction:
            pass
        else:
            diff_x = abs(atom.x - self.x)
            diff_y = abs(atom.y - self.y)



            # 상하방향 충돌
            if diff_x == 0:
                if {atom.direction, self.direction} == {0, 1}:
                    time = diff_y / 2
                    self.add_bomb(self, atom, time)
            # 좌우방향 충돌
            elif diff_y == 0:
                if {atom.direction, self.direction} == {2, 3}:
                    time = diff_x / 2
                    self.add_bomb(self, atom, time)

            # 대각선방향 충돌
            elif diff_x == diff_y:
                if {atom.direction, self.direction} in [{1, 3}, {1, 2}, {0, 3}, {0, 2}]:
                    time = diff_x
                    self.add_bomb(self, atom, time)


    @classmethod
    def add_bomb(cls, atom1, atom2, time):
        if time in cls.bomb:
            cls.bomb[time].append((atom1, atom2))
        else:
            cls.bomb[time] = [(atom1, atom2)]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    atoms = []

    for _ in range(N):
        x, y, direction, energy = map(int, input().split())
        atom = Atom(x, y, direction, energy)
        atoms.append(atom)

    for i in range(0, N - 1):
        for j in range(i, N):
            atoms[i].compare(atoms[j])

    total_energy = 0
    for time in Atom.bomb:
        bomb_atoms = set()
        for atom_set in Atom.bomb[time]:
            atom1, atom2 = atom_set

            if not atom1.is_dead and not atom2.is_dead:
                bomb_atoms.add(atom1)
                bomb_atoms.add(atom2)

        if bomb_atoms:
            for atom in bomb_atoms:
                total_energy += atom.e
                atom.is_dead = True

    print(total_energy)
