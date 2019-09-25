import sys

sys.stdin = open('sample_input.txt', 'r')


def BFS():
    global lands
    q = [(0, 0)]
    visited[0][0] = 0

    while q:
        i, j = q.pop(0)

        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in d:
            ni = i + dx
            nj = j + dy

            if 0 <= ni < N and 0 <= nj < N:
                # 연료 결정
                fuel = lands[ni][nj] - lands[i][j] + 1 if lands[ni][nj] > lands[i][j] else 1

                if visited[ni][nj] == -1:  # 아직 방문자체를 안했으면
                    visited[ni][nj] = visited[i][j] + fuel
                    q.append((ni, nj))

                elif visited[i][j] + fuel < visited[ni][nj]:  # 방문은 이미 했었는데, 지금 값이 더 작으면
                    visited[ni][nj] = visited[i][j] + fuel
                    q.append((ni, nj))

    return visited[N - 1][N - 1]  # 중간에 리턴하면 안된다. 마지막까지 바뀔 수 있어서..


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lands = [list(map(int, input().split())) for _ in range(N)]
    visited = [[-1] * N for _ in range(N)]

    print("#{} {}".format(tc, BFS()))
