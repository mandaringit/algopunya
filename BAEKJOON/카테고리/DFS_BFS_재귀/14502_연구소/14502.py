import sys

sys.stdin = open('input.txt', 'r')

from collections import deque
import copy


def BFS(lab):
    global virus_positions
    global N
    global M

    q = deque(virus_positions)
    visited = [[0] * M for _ in range(N)]

    while q:
        i, j = q.popleft()
        visited[i][j] = 1

        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in d:
            ni = i + dx
            nj = j + dy

            if 0 <= ni < N and 0 <= nj < M:
                if lab[ni][nj] == 0 and visited[ni][nj] == 0:
                    lab[ni][nj] = 2
                    q.append([ni, nj])
                    visited[ni][nj] = 1


N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

virus_positions = []

# 벽을 세울 수 있는 곳들을 찾자
possible_locations = set()

for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            virus_positions.append([i, j])

        if lab[i][j] == 0:
            possible_locations.add((i, j))

# 3개를 고르는 경우의 수를 만들자

subsets = []
p_count = len(possible_locations)
for i in range(p_count):
    for j in range(i + 1, p_count):
        for k in range(j + 1, p_count):
            pl = list(possible_locations)
            subset = [pl[i], pl[j], pl[k]]
            subsets.append(subset)

maxV = 0

for subset in subsets:

    # 랩 자체를 바꾸므로 딥카피해서 쓴다 (느리지만 어쩔수없엉)
    new_lab = copy.deepcopy(lab)

    # 벽을 세워보고
    for i, j in subset:
        new_lab[i][j] = 1

    # BFS 돌리고
    BFS(new_lab)

    # 0 카운트 => 안전지대
    count = 0
    for row in new_lab:
        count += row.count(0)

    if count > maxV:
        maxV = count

print(maxV)
