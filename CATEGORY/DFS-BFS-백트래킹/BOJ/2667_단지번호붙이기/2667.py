import sys

sys.stdin = open('input.txt', 'r')


def BFS(i, j, map, N, danji):
    q = [[i, j]]

    visited = []

    while q:
        k, m = q.pop(0)

        if [k, m] not in visited:
            visited.append([k, m])
            map[k][m] = danji

            d = [(0, -1), (0, 1), (1, 0), (-1, 0)]

            for dx, dy in d:

                ni = k + dx
                nj = m + dy

                if 0 <= ni < N and 0 <= nj < N:
                    if map[ni][nj] == '1':
                        q.append([ni, nj])

    return visited


N = int(input())

map = [list(input()) for _ in range(N)]

danji = 0

result = []

for i in range(N):
    for j in range(N):

        if map[i][j] == '1':
            danji += 1
            result.append(len(BFS(i, j, map, N, danji)))

print(danji)

result.sort()  # 단지에 번호를 매기는건 자기 맘이므로 오름차순으로 정렬해 놓으라는것.
for i in result:
    print(i)
