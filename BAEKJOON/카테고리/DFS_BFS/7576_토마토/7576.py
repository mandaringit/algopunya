# 시간초과
# list.pop(0), list.index, list.insert, list.count, x in list, list[:-1] 등은 다 O(N)입니다.
# list를 큐로 사용하면 절대, 절대, 절대, 절대, 절대 안 됩니다!! 큐는 반드시 collections.deque를 써야 합니다.
# 복사해서 비교해서 쓰니 통과했느ㅜㄴ데... 음..

import sys

sys.stdin = open('input.txt', 'r')


def BFS(q, N,M,baked_t_count, box, copy):
    max_day = 0

    while q:
        i, j = q.popleft()

        max_day = copy[i][j]  # 제일 큰 날은 가면 갈수록 늘어나니 가장 마지막것이 가장 큰것

        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in d:

            ni = i + dx
            nj = j + dy

            if 0 <= ni < N and 0 <= nj < M:

                if box[ni][nj] == 0 and copy[ni][nj] == 0:

                    q.append([ni, nj])
                    baked_t_count += 1
                    copy[ni][nj] = copy[i][j] + 1

    return max_day, baked_t_count


from collections import deque

M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]

copybox = [[0] * M for _ in range(N)]

q = deque()

baked_t_count = 0  # 이미 익은 토마토
t_count = 0  # 익힐 토마토
no_t_count = 0  # 토마토 없음

for i in range(N):
    for j in range(M):

        if box[i][j] == 1:
            q.append([i, j])
            baked_t_count += 1
        elif box[i][j] == 0:
            t_count += 1
        elif box[i][j] == -1:
            no_t_count += 1

if baked_t_count + no_t_count == N * M:
    print(0)
else:
    max_day, baked_t_count = BFS(q,N,M ,baked_t_count, box, copybox)
    if baked_t_count + no_t_count != N * M:
        print(-1)
    else:
        print(max_day)
