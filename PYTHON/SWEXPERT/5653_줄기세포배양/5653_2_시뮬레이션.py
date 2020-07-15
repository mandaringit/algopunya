import sys

sys.stdin = open('sample_input.txt', 'r')


class StemCell:
    _state = ['deactivate', 'activate', 'died']

    def __init__(self, i, j, life):
        self.i = i
        self.j = j
        self.life = life
        self.state = StemCell._state[0]
        self.time = 0

    def __str__(self):
        return "{},{} : {}, 생명력은 {}, {}초 지남".format(self.i, self.j, self.state, self.life, self.time)

    def reproduce(self):
        global cells

        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in d:
            ni = self.i+dx
            nj = self.j+dy

            # 이미 그리드에 존재하면
            if (ni, nj) in cells:
                sc = cells[(ni, nj)]
                # 갓 생성된 놈에다가, 체력이 자신보다 낮으면 체력만 변경해주자
                if sc.state == 'deactivate' and sc.time == 0 and sc.life < self.life:
                    sc.life = self.life
            else:
                # 아니면 생산
                cells[(ni, nj)] = StemCell(ni, nj, self.life)


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    initialize = [list(map(int, input().split())) for _ in range(N)]
    cells = {}
    for i in range(N):
        for j in range(M):
            life = initialize[i][j]
            if life > 0:
                cells[(i, j)] = StemCell(i, j, life)
    T = 0
    while T < K:
        T += 1
        now_cells = list(cells.values())
        for cell in now_cells:
            # 시간을 "먼저" 증가 시키고
            cell.time += 1

        for cell in now_cells:
            if cell.state != 'died':
                # 증가한 시간에 따른 행동양식
                if cell.state == 'deactivate' and cell.time == cell.life:
                    cell.state = StemCell._state[1]  # 활성상태로 변경
                    cell.time = 0  # 시간 초기화
                elif cell.state == 'activate' and cell.time == 1:
                    cell.reproduce()  # 번식

                if cell.state == 'activate' and cell.time == cell.life:
                    cell.state = StemCell._state[2]  # 사망

    count = 0
    for cell in cells.values():
        if cell.state != 'died':
            count += 1

    print("#{} {}".format(tc, count))
