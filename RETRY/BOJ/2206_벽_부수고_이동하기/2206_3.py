import sys

sys.stdin = open('input.txt', 'r')


def BFS():
    global visited
    global maps
    global N, M

    q = [(0, 0, 1)]
    visited[0][0] = 1  # 카운트 수, 뚫기 가능 수

    while q:
        i, j, crash = q.pop(0)

        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in d:
            ni = i + dx
            nj = j + dy

            if 0 <= ni < N and 0 <= nj < M:
                prev = visited[i][j]

                if visited[ni][nj] == 0:  # 아직 한번도 방문하지 않았을때

                    if maps[ni][nj] == '1' and crash:  # 벽일때, 뚫기 가능하면
                        visited[ni][nj] = prev + 1
                        q.append((ni, nj, 0))
                    elif maps[ni][nj] == '0':
                        visited[ni][nj] = prev + 1
                        q.append((ni, nj, crash))

                elif 0 < prev + 1 < visited[ni][nj]:  # 한번은 방문했지만, 지금 값이 더 작아질때
                    if maps[ni][nj] == '1' and crash:
                        visited[ni][nj] = prev + 1
                        q.append((ni, nj, 0))

                    elif maps[ni][nj] == '0':
                        visited[ni][nj] = prev + 1
                        q.append((ni, nj, crash))

                elif visited[ni][nj] == prev + 1 and crash:  # 같지만, 벽부수기가 가능할때
                    if maps[ni][nj] == '1' and crash:
                        visited[ni][nj] = prev + 1
                        q.append((ni, nj, 0))
                    elif maps[ni][nj] == '0':
                        visited[ni][nj] = prev + 1
                        q.append((ni, nj, crash))
    return visited[M - 1][N - 1]


N, M = map(int, input().split())

maps = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
BFS()
print(visited)  # 29
