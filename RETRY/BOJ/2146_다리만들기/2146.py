import sys

sys.stdin = open('input.txt', 'r')


# 92퍼센트에서 틀렸습니다
# 섬 라벨링 -> 토마토문제처럼 하나씩 BFS

# 라벨링용
def labeling(i, j, count):
    global new_maps
    global boundaries
    global d
    global visited

    new_maps[i][j] = count

    stack = [(i, j)]
    while stack:

        i_, j_ = stack.pop()

        for dx, dy in d:
            ni = i_ + dx
            nj = j_ + dy

            if 0 <= ni < N and 0 <= nj < N:
                if maps[ni][nj] == 0:
                    visited[i_][j_] = 0
                    boundaries.add((i_, j_, count))

                if new_maps[ni][nj] == 0 and maps[ni][nj] == 1:
                    new_maps[ni][nj] = count
                    stack.append((ni, nj))


def roadBFS():
    global boundaries
    global visited
    global maps, new_maps

    new_boundaries = list(boundaries)

    while new_boundaries:
        i, j, island_number = new_boundaries.pop(0)

        for dx, dy in d:
            ni = i + dx
            nj = j + dy

            if 0 <= ni < N and 0 <= nj < N:
                # 미방문 및 바다일때 및 새 지도에서도 아직 바다일때
                if visited[ni][nj] == -1 and maps[ni][nj] == 0 and new_maps[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    new_maps[ni][nj] = island_number
                    new_boundaries.append((ni, nj, island_number))

                # 방문은 했으나, 새 지도에서 바다가 아니고, 섬 번호가 자신이랑 다를때 (만났을때)
                elif visited[ni][nj] >= 0 and new_maps[ni][nj] != 0 and new_maps[ni][nj] != island_number:
                    print(visited[ni][nj] + visited[i][j])
                    return


N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

boundaries = set()
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
new_maps = [[0] * N for _ in range(N)]
visited = [[-1] * N for _ in range(N)]
count = 0
for i in range(N):
    for j in range(N):

        if maps[i][j] == 1 and new_maps[i][j] == 0:
            count += 1
            labeling(i, j, count)

roadBFS()
print(visited)