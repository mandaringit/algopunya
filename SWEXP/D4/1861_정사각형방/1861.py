import sys

sys.stdin = open('input.txt', 'r')


def BFS(i, j):
    global max_count, max_room
    global N
    global rooms

    q = [(i, j)]

    while q:
        i_, j_ = q.pop(0)

        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in d:
            ni = i_ + dx
            nj = j_ + dy

            # 인덱스 범위안이고, 다음 방이 지금 방보다 딱 1이 더큰가?
            if 0 <= ni < N and 0 <= nj < N:
                if rooms[ni][nj] == rooms[i_][j_] + 1:

                    # 그렇다면 다음방의 지금까지 BFS를 통해 결정된 최대 방수는 몇인가?
                    max_d = visited[ni][nj]

                    # 아직 방문하지 않았거나 == 1
                    # 이미 최대거리가 있지만, 그 값이 현재의 최대거리보다 작다면 -> 갱신하고 다시 큐에 넣는다.
                    if 1 <= max_d < visited[i_][j_] + 1:
                        visited[ni][nj] = visited[i_][j_] + 1  # 갱신

                        if visited[ni][nj] > max_count:  # 크기 비교 및 max값 결정
                            max_count = visited[ni][nj]
                            max_room = rooms[i][j]
                        elif visited[ni][nj] == max_count:  # 동일한 크기라면 방값이 작은걸로 교체
                            if rooms[i][j] < max_room:
                                max_room = rooms[i][j]

                        q.append((ni, nj))  # 인큐

                    # 현재 최대거리보다 큰 경우는 굳이 다시 큐로 들어갈 필요가 없다.
                    # 어차피 같은 길을 갈거고, 그 값은 지금보다 더 작아져서 쓸모가 없을테니까.


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    max_room = 0
    max_count = 0

    # 방은 모두 자기자신 하나만 들를 수 있는, 최소 1의 최대거리를 가지고 있다.
    visited = [[1] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 아직 다른좌표에서 오지 않아, BFS로 돌지 않은 장소만 탐색을 하러 간다.
            if visited[i][j] == 1:
                BFS(i, j)

    print("#{} {} {}".format(tc, max_room, max_count))
