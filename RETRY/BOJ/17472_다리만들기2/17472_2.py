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
    island_set = []
    count = 0
    for idx, value in enumerate(line):
        if value > 0 and value not in island_set:
            island_set.append(value)
            if len(island_set) == 2:
                key = (island_set[0], island_set[1])
                if count >= 2:
                    if key in adj:
                        if adj[key][2] > count:
                            adj[key] = [island_set[0], island_set[1], count]
                    else:
                        adj[key] = [island_set[0], island_set[1], count]
                count = 0
                island_set.pop(0)
        elif value == 0 and len(island_set) == 1:
            count += 1


def rep(n, p):
    while n != p[n]:
        n = p[n]
    return n


def kruskal():
    global count
    global adj

    T = []
    p = [0] + [i for i in range(1, count + 1)]
    edges = list(adj.keys())
    edges.sort(key=lambda x: adj[x][2])  # 간선 가중치 별로 정렬

    total_weight = 0
    N = 0
    for edge in edges:
        n1, n2, weight = adj[edge]
        represent1 = rep(n1, p)
        represent2 = rep(n2, p)
        if represent1 != represent2:
            total_weight += weight
            p[represent1] = represent2
            N += 1
            if N == count:
                break

    return total_weight


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
labeling = [[0] * M for _ in range(N)]

# 섬 구분
count = 0
adj = {}
for i in range(N):
    for j in range(M):
        if maps[i][j] == 1 and labeling[i][j] == 0:
            count += 1
            dividing(i, j, count)

for row in labeling:
    get_adj(row)

col_labeling = zip(*labeling)
for col in col_labeling:
    get_adj(col)

if len(adj) >= count - 1:
    w = kruskal()
    print(w)
else:
    print(-1)

