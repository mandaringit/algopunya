import sys

sys.stdin = open('sample_input.txt', 'r')


class Person:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, cmd):
        if cmd == 0:
            pass
        elif cmd == 1:
            self.y -= 1
        elif cmd == 2:
            self.x += 1
        elif cmd == 3:
            self.y += 1
        elif cmd == 4:
            self.x -= 1

    def is_possible_bc(self, bc):
        return abs(bc.x - self.x) + abs(bc.y - self.y) <= bc.C


class BC:

    def __init__(self, x, y, C, P):
        self.x = x
        self.y = y
        self.C = C
        self.P = P


def get_maximum_bc(p1_possible_list, p2_possible_list):
    max_sum_of_p = 0

    # 둘중 하나가 아무것도 없을때
    if not p1_possible_list:
        for p2bc in p2_possible_list:
            if p2bc.P > max_sum_of_p:
                max_sum_of_p = p2bc.P

    elif not p2_possible_list:
        for p1bc in p1_possible_list:
            if p1bc.P > max_sum_of_p:
                max_sum_of_p = p1bc.P

    # 둘 다 있을때
    else:
        for p1bc in p1_possible_list:
            for p2bc in p2_possible_list:

                possible_bc_set = {p1bc, p2bc}

                if len(possible_bc_set) == 1:
                    sum_of_p = list(possible_bc_set)[0].P
                else:
                    sum_of_p = p1bc.P + p2bc.P

                if sum_of_p > max_sum_of_p:
                    max_sum_of_p = sum_of_p

    return max_sum_of_p


def check_p(p1, p2, BCs):
    p1_possible = []
    p2_possible = []

    for bc in BCs:
        if p1.is_possible_bc(bc):
            p1_possible.append(bc)

        if p2.is_possible_bc(bc):
            p2_possible.append(bc)

    return get_maximum_bc(p1_possible, p2_possible)


T = int(input())

for tc in range(1, T + 1):
    M, A = map(int, input().split())  # 이동시간, BC개수

    p1_command = list(map(int, input().split()))
    p2_command = list(map(int, input().split()))

    BCs = []
    # BC 정보
    for _ in range(A):
        x, y, c, p = map(int, input().split())
        bc = BC(x, y, c, p)
        BCs.append(bc)

    p1 = Person(1, 1)
    p2 = Person(10, 10)

    total = 0

    # 움직이기 전에 한번 체크

    total += check_p(p1, p2, BCs)

    for i in range(len(p1_command)):
        p1.move(p1_command[i])
        p2.move(p2_command[i])

        total += check_p(p1, p2, BCs)

    print("#{} {}".format(tc, total))
