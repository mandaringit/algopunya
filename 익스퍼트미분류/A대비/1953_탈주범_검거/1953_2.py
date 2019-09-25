import sys

sys.stdin = open('sample_input.txt', 'r')


def tunneling(N, M):
    global tunnel_map
    global tunnel
    global R
    global C
    global L
    # 상 하 좌 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 상 하 좌 우 순
    possible_structure = [(1, 2, 5, 6), (1, 2, 4, 7), (1, 3, 4, 5), (1, 3, 6, 7)]
    # 배관별 이동 가능 방향
    idxs = [(0, 1, 2, 3), (0, 1), (2, 3), (0, 3), (1, 3), (1, 2), (0, 2)]
    tunnel_number = 1

    q = [[R, C, 0]]

    while q:
        i, j, time = q.pop(0)
        tunnel[i][j] = tunnel_number

        type = tunnel_map[i][j]  # 자신의 타입

        d_idx = idxs[type - 1]

        for idx in d_idx:
            dx, dy = directions[idx]

            ni = i + dx
            nj = j + dy

            # 범위 안이고,
            if 0 <= ni < N and 0 <= nj < M:
                # 아직 공사 안했고, 연결 가능한 경우 일 때,
                is_structure_exist = tunnel[ni][nj]
                compare_type = tunnel_map[ni][nj]
                possible_type = possible_structure[idx]
                if not is_structure_exist and compare_type in possible_type and time + 1 < L:
                    q.append([ni, nj, time + 1])


T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())

    tunnel_map = [list(map(int, input().split())) for _ in range(N)]
    tunnel = [[0] * M for _ in range(N)]

    tunneling(N, M)
    total = 0
    for row in tunnel:
        total += row.count(1)
    print("#{} {}".format(tc, total))
