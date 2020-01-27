import sys
from collections import deque

sys.stdin = open('input.txt', 'r')


def BFS(shark):
    global area, N, eating, shark_size
    visited = [[-1] * N for _ in range(N)]
    visited[shark[0]][shark[1]] = 0

    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    Q = deque()
    Q.append(shark)

    fishes = {}
    while len(Q) != 0:
        i, j = Q.popleft()

        for dx, dy in d:
            ni = i + dx
            nj = j + dy

            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == -1:
                    # 아무것도 없을때 또는 자기랑 사이즈가 같을때 => 지나간다
                    if area[ni][nj] == 0 or area[ni][nj] == shark_size:
                        Q.append([ni, nj])
                        visited[ni][nj] = visited[i][j] + 1
                    # 자기보다 작을때 => 먹을 리스트에 저장
                    elif area[ni][nj] < shark_size:
                        visited[ni][nj] = visited[i][j] + 1
                        diff = visited[i][j] + 1
                        if diff in fishes:
                            fishes[diff].append([ni, nj])
                        else:
                            fishes[diff] = [[ni, nj]]
                        # 자기보다 클때 => 못지나감
                    else:
                        pass
    return fishes


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

# 상어 위치 찾기
shark = None
shark_size = 2
total_time = 0
eating = 0
for i in range(N):
    for j in range(N):
        if area[i][j] == 9:
            shark = [i, j]
            area[i][j] = 0

# 탐색


while True:
    fishes = BFS(shark=shark)

    if not fishes:
        break

    min_d = sorted(list(fishes.keys()))[0]
    min_i, min_j = N, N
    if len(fishes[min_d]) > 1:
        for f_i, f_j in fishes[min_d]:
            if f_i < min_i:
                min_i, min_j = f_i, f_j
            elif f_i == min_i and f_j < min_j:
                min_i, min_j = f_i, f_j
    else:
        min_i, min_j = fishes[min_d][0]

    total_time += min_d
    eating += 1

    if shark_size == eating:
        eating = 0
        shark_size += 1

    area[min_i][min_j] = 0
    shark = min_i, min_j

print(total_time)
