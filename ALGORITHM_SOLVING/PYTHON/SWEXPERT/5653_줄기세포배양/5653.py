import sys

sys.stdin = open('sample_input.txt', 'r')


class StemCell:

    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.life = hp  # 생명력 기준
        self.hp = hp  # 깎을 생명력
        self.activate = False  # 활성여부
        self.passed_time = 0  # 생긴 이후 지난 시간
        self.dead = False  # 사망 여부

    def reproduce(self):
        global stems

        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in d:
            nx = self.x + dx
            ny = self.y + dy

            coord = (nx, ny)

            # 이미 생성된 좌표라면
            if coord in stems:
                exist_sc = stems[coord]
                if exist_sc.passed_time == 0 and exist_sc.life < self.life:
                    exist_sc.life = self.life
                    exist_sc.hp = self.life

            else:
                new_sc = StemCell(nx, ny, self.life)
                stems[(nx, ny)] = new_sc


T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # 세로 가로 배양시간

    grid = [list(map(int, input().split())) for _ in range(N)]

    stems = {}

    # 초기 줄기세포 저장
    for i in range(N):
        for j in range(M):
            if grid[i][j] > 0:
                sc = StemCell(i, j, grid[i][j])
                stems[(i, j)] = sc


    # K 회 돌기
    hour = 0
    while hour < K:
        hour += 1

        # 현재 존재하는 줄기세포들의 시간을 1 증가시킨다.
        for stem_cell in stems.values():
            stem_cell.passed_time += 1

        # 시간이 증가된 줄기세포들만을 보고 프로세스를 진행한다.
        this_time_cells = list(stems.values())
        for stem_cell in this_time_cells:

            # 해당 셀이 활성화 되어 있다면
            if stem_cell.activate:

                # 첫 한시간동안 번식한다.
                if stem_cell.passed_time == stem_cell.life + 1:
                    stem_cell.reproduce()

                # 활성화 된 이후부터 피가 1씩 깎인다.
                if stem_cell.passed_time > stem_cell.life:
                    stem_cell.hp -= 1

                    if stem_cell.hp == 0:
                        stem_cell.dead = True
                        stem_cell.activate = False

            # 경과 시간이 생명력 수치와 같아질때 활성화 시키기.
            if stem_cell.passed_time == stem_cell.life:
                stem_cell.activate = True

    count = 0

    for sc in stems.values():
        if not sc.dead:
            count += 1
    print("#{} {}".format(tc, count))
