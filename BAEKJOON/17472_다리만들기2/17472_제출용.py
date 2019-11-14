import sys

sys.stdin = open('input2.txt', 'r')


def dividing(i, j, count):
    global maps, N, M, labeling
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    stack = [(i, j)]
    labeling[i][j] = count

    while stack:
        i_, j_ = stack.pop()

        for dx, dy in d:
            ni = i_+dx
            nj = j_+dy

            if 0 <= ni < N and 0 <= nj < M:
                if maps[ni][nj] == 1 and labeling[ni][nj] == 0:
                    labeling[ni][nj] = count
                    stack.append((ni, nj))


def get_adj(line):
    global adj
    island_set = []
    weight = 0
    for idx, value in enumerate(line):
        if value > 0:
            if value not in island_set:
                island_set.append(value)
                # 섬이 두개 모이고, 그 길이가 2 이상이면
                if len(island_set) == 2 and weight >= 2:
                    i1 = island_set[0]
                    i2 = island_set[1]
                    G[i1].add(i2)
                    G[i2].add(i1)
                    # 이미 가중치가 있었으면, 가중치가 현재보다 작아지는 경우에만
                    if (i1, i2) in adj:
                        if weight < adj[(i1, i2)][2]:
                            adj[(i1, i2)] = [i1, i2, weight]
                    else:
                        adj[(i1, i2)] = [i1, i2, weight]

                    weight = 0
                    island_set.pop(0)
                elif len(island_set) == 2 and weight < 2:
                    island_set.pop(0)
                    weight = 0
            else:
                weight = 0

        elif value == 0 and len(island_set) == 1:
            weight += 1


def is_all_connected(G):
    global i_count
    stack = [1]
    visited = {1}

    while stack:
        node = stack.pop()
        for u in G[node]-visited:
            visited.add(u)
            stack.append(u)

    if len(visited) == i_count:
        return True
    else:
        return False


def rep(n, p):
    while n != p[n]:
        n = p[n]
    return n


def kruskal():
    global i_count
    global adj

    p = [0]+[i for i in range(1, i_count+1)]
    edges = list(adj.values())
    edges.sort(key=lambda x: x[2])  # 간선 가중치 별로 정렬

    total_weight = 0
    N = 0
    for edge in edges:
        n1, n2, weight = edge
        represent1 = rep(n1, p)
        represent2 = rep(n2, p)
        if represent1 != represent2:
            total_weight += weight
            p[represent1] = represent2
            N += 1
            if N == i_count-1:
                break

    return total_weight


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
labeling = [[0]*M for _ in range(N)]

# 섬 구분
i_count = 0  # 섬 갯수
for i in range(N):
    for j in range(M):
        if maps[i][j] == 1 and labeling[i][j] == 0:
            i_count += 1
            dividing(i, j, i_count)

# 그래프, 가중치
G = {i: set() for i in range(1, i_count+1)}
adj = {}

# 섬간의 인접길이(가중치)구하기
for row in labeling:
    get_adj(row)
col_labeling = zip(*labeling)
for col in col_labeling:
    get_adj(col)

if is_all_connected(G):
    print(kruskal())
else:
    print(-1)
