import sys

sys.stdin = open('sample_input.txt', 'r')


class Atom:

    def __init__(self, x, y, direction, e):
        self.x = x
        self.y = y
        self.direction = direction
        self.e = e

    def move(self, sec):

        if self.direction == 0:
            self.y += sec
        elif self.direction == 1:
            self.y -= sec
        elif self.direction == 2:
            self.x -= sec
        elif self.direction == 3:
            self.x += sec

        return self.x, self.y


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    atoms = []

    for _ in range(N):
        x, y, direction, energy = map(int, input().split())
        atom = Atom(x, y, direction, energy)
        atoms.append(atom)

    dead_atoms = set()

    count = 0
    while count < 4000:
        count += 1
        sec = 0.5

        dead = set()
        live_atoms = []

        for atom in atoms:
            atom.move(sec)

            for another_atom in live_atoms:
                if atom.x == another_atom.x and atom.y == another_atom.y:
                    dead.add(atom)
                    dead.add(another_atom)

            live_atoms.append(atom)

        for atom in dead:
            dead_atoms.add(atom)
            atoms.remove(atom)

    total_energy = 0

    for atom in dead_atoms:
        total_energy += atom.e
    print(total_energy)