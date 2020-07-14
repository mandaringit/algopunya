import sys

sys.stdin = open('input.txt', 'r')


def look_around(i, j):
    global table
    global N

    d = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

    mine = 0
    locations = []
    for dx, dy in d:
        ni = i + dx
        nj = j + dy

        if 0 <= ni < N and 0 <= nj < N:
            if table[ni][nj] == '.':
                locations.append([ni, nj])  # 만약 지뢰가 없으면 이따가 탐색할 곳들을 모아두자

            elif table[ni][nj] == '*':
                mine += 1

    table[i][j] = mine

    if not mine:
        # 주변도 탐색해주기
        for nni, nnj in locations:
            look_around(nni, nnj)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    table = [list(input()) for _ in range(N)]

    count = 0

    for i in range(N):
        for j in range(N):
            # 본인이 지뢰 또는 숫자가 아니고
            if table[i][j] == '.':
                d = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
                is_mine_exist = False

                for dx, dy in d:
                    ni = i + dx
                    nj = j + dy

                    if 0 <= ni < N and 0 <= nj < N:
                        if table[ni][nj] == '*':
                            is_mine_exist = True
                            break

                # 주변에 지뢰가 하나도 없을때
                if not is_mine_exist:
                    table[i][j] = 0
                    count += 1
                    # 해당 자리에서 탐색시작(자기 자신 기준에서 주변 변화시키기)
                    look_around(i, j)

    # 더이상 위와 같은 점이 없으면 마지막으로 남은 점('.')의 개수만큼 클릭
    for i in range(N):
        for j in range(N):
            if table[i][j] == '.':
                count += 1

    print("#{} {}".format(tc, count))
