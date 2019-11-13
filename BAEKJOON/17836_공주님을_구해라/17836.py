import sys

sys.stdin = open('input.txt', 'r')

def BFS():
    global N, M, T, visited, castle
    global gram_time
    d = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    visited[0][0] = 0

    Q = [(0, 0)]

    while Q:
        i, j = Q.pop(0)
        time = visited[i][j]

        for dx, dy in d:
            ni = i+dx
            nj = j+dy

            # 범위안 + 미방문
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1:
                next_time = time+1
                # 1. 시간이 아직 괜찮다면
                if next_time <= T:
                    value = castle[ni][nj]

                    if (ni, nj) == (N-1, M-1):
                        return next_time

                    elif value in [0, 2]:

                        if value == 2:  # 만약 그람을 찾았다면..!
                            shortcut_d = abs(ni-(N-1))+abs(nj-(M-1))
                            arrive_time = next_time+shortcut_d
                            if arrive_time <= T:
                                gram_time = arrive_time

                        visited[ni][nj] = next_time
                        Q.append((ni, nj))
    return 'Fail'


N, M, T = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
gram_time = 100000000
time = BFS()

if time == 'Fail' and gram_time == 100000000:
    print('Fail')
elif time == 'Fail' and gram_time <= T:
    print(gram_time)
else:
    if time > gram_time:
        print(gram_time)
    else:
        print(time)

