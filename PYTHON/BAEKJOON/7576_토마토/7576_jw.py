def bfs(start, box, sample, q_size):

    q = [0] * q_size
    front = -1
    rear = -1

    for i in range(len(start)):
        rear += 1
        q[rear] = start[i]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    cnt = 0
    x, y = 0, 0

    while True:
        if front == rear:
            break

        front += 1
        now = q[front]
        x, y = now

        for k in range(4):
            x_ = x + dx[k]
            y_ = y + dy[k]

            if 0 <= x_ < M and 0 <= y_ < N:

                if box[x_][y_] == 0 and sample[x_][y_] == 0:
                    rear += 1
                    q[rear] = [x_, y_]
                    sample[x_][y_] = sample[x][y] + 1
                    cnt += 1

    return sample[x][y], cnt


N, M = map(int, input().split())
box = [list(map(int, input().split())) for i in range(M)]

start = []
sample = [[0] * N for m in range(M)]
size = N * M
none_cnt = 0
cnt = 0
dis_cnt = 0

for i in range(M):
    for j in range(N):
        target = box[i][j]
        if target == 1:
            start.append([i, j])
            cnt += 1
        if target == 0:
            none_cnt += 1
        if target == -1:
            dis_cnt += 1

if cnt + dis_cnt == size:
    print(0)
else:
    q_size = none_cnt + cnt
    a, change = bfs(start, box, sample, q_size)
    if none_cnt == change:
        print(a)
    else:
        print(-1)
