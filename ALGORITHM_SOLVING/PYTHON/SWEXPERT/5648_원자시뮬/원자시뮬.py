import sys

sys.stdin = open('sample_input.txt', 'r')


class Atom:
    def __init__(self, x, y, direction, e):
        self.x = x
        self.y = y
        self.direction = direction
        self.e = e
        self.is_dead = False  # 터지면 True로 변경됨

    def move(self, time):
        moved_x = self.x
        moved_y = self.y

        if self.direction == 0:
            moved_y += time
        elif self.direction == 1:
            moved_y -= time
        elif self.direction == 2:
            moved_x -= time
        elif self.direction == 3:
            moved_x += time

        return moved_x, moved_y


def add_bomb(bome_times, atom1, atom2, time):
    if time in bome_times:
        bome_times[time].append((atom1, atom2))
    else:
        bome_times[time] = [(atom1, atom2)]


# 터질 수 있는 가능성을 검사 및 가능성있는 시간 구하기
def compare(bomb_times, atom1, atom2):
    if atom1.direction == atom2.direction:
        pass
    else:
        diff_x = abs(atom1.x - atom2.x)
        diff_y = abs(atom1.y - atom2.y)

        # 상하방향 충돌
        if diff_x == 0:
            if {atom1.direction, atom2.direction} == {0, 1}:
                time = diff_y / 2
                add_bomb(bomb_times, atom1, atom2, time)

        # 좌우방향 충돌
        elif diff_y == 0:
            if {atom1.direction, atom2.direction} == {2, 3}:
                time = diff_x / 2
                add_bomb(bomb_times, atom1, atom2, time)

        # 대각선방향 충돌
        elif diff_x == diff_y:
            if {atom1.direction, atom2.direction} in [{1, 3}, {1, 2}, {0, 3}, {0, 2}]:
                time = diff_x
                add_bomb(bomb_times, atom1, atom2, time)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 받은 원자들 저장
    atoms = []
    for _ in range(N):
        x, y, direction, energy = map(int, input().split())
        atom = Atom(x, y, direction, energy)  # 원자 인스턴스 생성
        atoms.append(atom)

    bomb_times = {}  # 시간별 충돌 가능성이 있는 쌍들을 저장

    # 두 쌍씩 비교하면서 가능성을 살펴본다.
    for i in range(0, N - 1):
        for j in range(i, N):
            compare(bomb_times, atoms[i], atoms[j])


    total_energy = 0

    for time in sorted(bomb_times):  # 시간순서대로 진행해보자.
        bomb_atoms = set()  # 터뜨릴 원자들을 저장. (혹시나 중복을 피하기 위해 셋으로.)

        for atom_set in bomb_times[time]:
            atom1, atom2 = atom_set

            # 터진다면, 터지기 0.5초전 각 원자의 좌표
            (prev_x1, prev_y1), (prev_x2, prev_y2) = atom1.move(time - 0.5), atom2.move(time - 0.5)

            # 터진다면, 터질때의 각 원자 좌표들
            (x1, y1), (x2, y2) = atom1.move(time), atom2.move(time)

            # 두 점 사이의 거리는 (x2 - x1)^2 + (y2 - y1)^2  여기에 루트 씌우기. 둘다 루트 씌워야 하므로 생략했음.
            prev_distance = ((prev_x2 - prev_x1) ** 2 + (prev_y2 - prev_y1) ** 2)
            now_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2)

            # 이전거리에 비해 지금 거리가 줄었고(가까워진다는 뜻), 두 원자가 모두 안죽은 상태일때
            if prev_distance > now_distance and not atom1.is_dead and not atom2.is_dead:
                bomb_atoms.add(atom1)
                bomb_atoms.add(atom2)

        # 모아놓은 원자들을 터뜨리면서 에너지를 가져오자
        if bomb_atoms:
            for atom in bomb_atoms:
                total_energy += atom.e
                atom.is_dead = True

    print("#{} {}".format(tc, total_energy))
