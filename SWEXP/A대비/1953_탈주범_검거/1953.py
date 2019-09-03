import sys

sys.stdin = open('sample_input.txt', 'r')


def tunneling(N, M):
    global tunnel_map
    global tunnel

    # 상 하 좌 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 상 하 좌 우 순
    possible_structure = [(1, 2, 5, 6), (1, 2, 4, 7), (1, 3, 4, 5), (1, 3, 6, 7)]

    tunnel_number = 0

    for i in range(N):
        for j in range(M):

            # 터널 지도를 보고 수로를 지어야 하고,
            # 아직 터널을 안뚫었을때
            if tunnel_map[i][j] > 0 and tunnel[i][j] == 0:
                tunnel_number += 1
                stack = [[i, j]]

                while stack:
                    i_, j_ = stack.pop()
                    tunnel[i_][j_] = tunnel_number

                    type = tunnel_map[i_][j_]  # 자신의 타입

                    if type == 1:
                        # 상 하 좌 우
                        d_idx = (0, 1, 2, 3)
                    elif type == 2:
                        # 상하
                        d_idx = (0, 1)
                    elif type == 3:
                        # 좌우
                        d_idx = (2, 3)
                    elif type == 4:
                        # 상우
                        d_idx = (0, 3)
                    elif type == 5:
                        # 하우
                        d_idx = (1, 3)
                    elif type == 6:
                        # 하좌
                        d_idx = (1, 2)
                    elif type == 7:
                        # 상좌
                        d_idx = (0, 2)

                    for idx in d_idx:
                        dx, dy = directions[idx]

                        ni = i_ + dx
                        nj = j_ + dy

                        # 범위 안이고,
                        if 0 <= ni < N and 0 <= nj < M:
                            # 아직 공사 안했고, 터널 맵에 숫자가 존재하며 , 가능한 경우 일 때,
                            is_structure_exist = tunnel[ni][nj]
                            compare_type = tunnel_map[ni][nj]
                            possible_type = possible_structure[idx]
                            if not is_structure_exist and compare_type in possible_type:
                                stack.append([ni, nj])


T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())

    tunnel_map = [list(map(int, input().split())) for _ in range(N)]
    tunnel = [[0] * M for _ in range(N)]

    tunneling(N, M)

    # 이제 tunnel의 출발점에서 시작해, 해당 깊이까지 갈때 갈 수 있는 모든 장소의 수를 세면 된다.
