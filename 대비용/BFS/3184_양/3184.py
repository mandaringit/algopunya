import sys

sys.stdin = open('input.txt', 'r')


def DFS(i, j):
    global maps
    global visited
    global R, C
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visited[i][j] = 1
    stack = [(i, j)]

    animal_count = {
        'v': 0,
        'o': 0
    }

    animal_count[maps[i][j]] += 1

    while stack:
        i_, j_ = stack.pop()

        for dx, dy in d:
            ni = i_ + dx
            nj = j_ + dy

            if 0 <= ni < R and 0 <= nj < C:
                if maps[ni][nj] != '#' and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    value = maps[ni][nj]
                    stack.append((ni, nj))
                    if value in ['o', 'v']:
                        animal_count[value] += 1
            else:
                # 영역이 아님
                return False

    if animal_count['v'] >= animal_count['o']:
        animal_count['o'] = 0
    else:
        animal_count['v'] = 0

    return animal_count


R, C = map(int, input().split())  # 행 ,열

maps = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

# 동물들 위치 찾기.
animals = []
for i in range(R):
    for j in range(C):
        if maps[i][j] in ['o', 'v']:
            animals.append((i, j, maps[i][j]))

total_animals = {
    'v': 0,
    'o': 0
}

for i, j, _ in animals:
    if visited[i][j] == 0:
        counts = DFS(i, j)
        if counts:
            total_animals['v'] += counts['v']
            total_animals['o'] += counts['o']

print(total_animals['o'], total_animals['v'])
