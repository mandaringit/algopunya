import sys

sys.stdin = open('input.txt', 'r')


def dividing(i, j, count):
    global maps, N, M, labeling
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    stack = [(i, j)]
    labeling[i][j] = count

    while stack:
        i_, j_ = stack.pop()

        for dx, dy in d:
            ni = i_ + dx
            nj = j_ + dy

            if 0 <= ni < N and 0 <= nj < M:
                if maps[ni][nj] == 1 and labeling[ni][nj] == 0:
                    labeling[ni][nj] = count
                    stack.append((ni, nj))


def get_adj(line):
    global adj
    island_set = []
    weight = 0
    for idx, value in enumerate(line):
        if value > 0 and value not in island_set:
            island_set.append(value)
            if len(island_set) == 2 and weight >= 2:
                if adj[island_set[0]][island_set[1]] > 0:
                    if weight < adj[island_set[0]][island_set[1]]:
                        adj[island_set[0]][island_set[1]] = weight
                        adj[island_set[1]][island_set[0]] = weight
                else:
                    adj[island_set[0]][island_set[1]] = weight
                    adj[island_set[1]][island_set[0]] = weight

                weight = 0
                island_set.pop(0)
        elif value == 0 and len(island_set) == 1:
            weight += 1


def perm(n, k):
    global islands
    global adj, minW

    if n == k:
        total_w = 0
        for idx in range(k - 1):
            i1 = islands[idx]
            i2 = islands[idx + 1]
            w = adj[i1][i2]
            if w == 0:
                return
            else:
                total_w += w

        if total_w < minW:
            minW = total_w
    else:
        for i in range(n, k):
            islands[n], islands[i] = islands[i], islands[n]
            perm(n + 1, k)
            islands[n], islands[i] = islands[i], islands[n]


# T = int(input())
# for tc in range(1, T + 1):
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
labeling = [[0] * M for _ in range(N)]

# 섬 구분
count = 0
for i in range(N):
    for j in range(M):
        if maps[i][j] == 1 and labeling[i][j] == 0:
            count += 1
            dividing(i, j, count)

adj = [[0] * (count + 1) for _ in range(count + 1)]
for row in labeling:
    get_adj(row)

col_labeling = zip(*labeling)
for col in col_labeling:
    get_adj(col)

islands = [i for i in range(1, count + 1)]
minW = 1000000000
perm(0, count)
if minW == 1000000000:
    print(-1)
else:
    print(minW)
