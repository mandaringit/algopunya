import sys

sys.stdin = open('input.txt', 'r')


def DFS(idx, path):
    global area, cctvs, minV, N, M, types
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # 마지막이면 계산후 종료
    if idx == len(cctvs):
        check_map = [[0] * M for _ in range(N)]

        for index, value in enumerate(cctvs):
            i_, j_ = value
            typ = area[i_][j_]
            selected_direction = path[index]
            look_d = types[typ][selected_direction]
            for seq in look_d:
                dx, dy = directions[seq]
                ni = i_ + dx
                nj = j_ + dy
                while True:

                    if 0 <= ni < N and 0 <= nj < M:
                        if area[ni][nj] == 6:
                            break
                        elif area[ni][nj] in [1, 2, 3, 4, 5]:
                            pass
                        else:
                            check_map[ni][nj] = '#'
                    else:
                        break

                    ni = ni + dx
                    nj = nj + dy
        count = 0
        for x in range(N):
            for y in range(M):
                if check_map[x][y] == '#':
                    count += 1

        total_no_cctv_zone_count = N * M - count - wall_count - len(cctvs)
        if total_no_cctv_zone_count < minV:
            minV = total_no_cctv_zone_count
        return

    i, j = cctvs[idx]
    cctv_type = area[i][j]

    if cctv_type == 1:
        d = [0, 1, 2, 3]
    elif cctv_type == 2:
        d = [0, 1]
    elif cctv_type == 3:
        d = [0, 1, 2, 3]
    elif cctv_type == 4:
        d = [0, 1, 2, 3]
    elif cctv_type == 5:
        d = [0]

    for next_d in d:
        DFS(idx + 1, path + [next_d])


N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]

types = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0]],
    5: [[0, 1, 2, 3]]
}

minV = N * M
cctvs = []
wall_count = 0
for i in range(N):
    for j in range(M):
        if area[i][j] in [1, 2, 3, 4, 5]:
            cctvs.append([i, j])
        elif area[i][j] == 6:
            wall_count += 1

DFS(0, [])
print(minV)
