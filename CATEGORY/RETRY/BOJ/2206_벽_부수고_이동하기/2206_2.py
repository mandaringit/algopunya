import sys

sys.stdin = open('input.txt', 'r')


def BFS():
    global visited
    global maps
    global N, M

    q = [(0, 0, 1)]
    visited[0][0] = (1, 1)  # 카운트 수, 뚫기 가능 수

    while q:
        i, j, crash = q.pop(0)

        if (i, j) == (N - 1, M - 1):
            return visited[i][j][0]

        else:
            d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in d:
                ni = i + dx
                nj = j + dy

                if 0 <= ni < N and 0 <= nj < M:
                    prev = visited[i][j][0]

                    if visited[ni][nj] == 0:  # 아직 한번도 방문하지 않았을때
                        if maps[ni][nj] == '1' and crash:  # 벽일때, 뚫기 가능하면
                            visited[ni][nj] = (prev + 1, 0)
                            if (ni, nj) == (N - 1, M - 1):
                                return prev + 1
                            else:
                                q.append((ni, nj, 0))

                        elif maps[ni][nj] == '0':
                            visited[ni][nj] = (prev + 1, crash)
                            if (ni, nj) == (N - 1, M - 1):
                                return prev + 1
                            else:
                                q.append((ni, nj, crash))

                    else:
                        if 0 < prev + 1 < visited[ni][nj][0]:
                            if maps[ni][nj] == '1' and crash:
                                visited[ni][nj] = (prev + 1, 0)
                                q.append((ni, nj, 0))

                            elif maps[ni][nj] == '0':
                                visited[ni][nj] = prev + 1
                                q.append((ni, nj, crash))

                        elif visited[ni][nj][0] == prev + 1 and visited[ni][nj][1] == 0 and crash:  # 같지만, 벽부수기가 가능할때
                            if maps[ni][nj] == '1' and crash:
                                visited[ni][nj] = (prev + 1, 0)
                                q.append((ni, nj, 0))
                            elif maps[ni][nj] == '0':
                                visited[ni][nj] = (prev + 1, 1)
                                q.append((ni, nj, crash))

    return -1


N, M = map(int, input().split())

maps = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
print(BFS())  # 29
