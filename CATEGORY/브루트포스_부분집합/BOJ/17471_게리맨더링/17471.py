# 1. 구역을 두개로 나눈다 (부분집합)
# 2. 두개로 나눈 그룹이 가능한 그룹인지 확인한다
# 3. 가능하면 인구 차이를 최소로 하는 경우를 구한다.

import sys

sys.stdin = open('input.txt', 'r')


def check_area(areas, graph):
    start = areas[0]
    visited = {start}

    q = [start]
    while q:

        area = q.pop(0)
        for nearby in graph[area] - visited:
            if nearby in areas:
                visited.add(nearby)
                q.append(nearby)

    if visited == set(areas):
        return True

    return False


N = int(input())  # 구역의 개수
populations = [0] + list(map(int, input().split()))
graph = {i: set() for i in range(1, N + 1)}

# 구역 그래프 생성
for i in range(1, N + 1):
    info = list(map(int, input().split()))
    area_count = info[0]
    area_numbers = info[1:]

    for area in area_numbers:
        graph[i].add(area)

minV = N * 100
# 구역을 두개로 나눈다
areas = list(graph.keys())
for i in range(1, 1 << N - 1):  # 두개로 나눠지지 않는 경우는 제외
    area1 = []
    area2 = []
    for j in range(N):
        if i & (1 << j):
            area1.append(areas[j])
        else:
            area2.append(areas[j])

    is_area1_possible = check_area(area1, graph)
    is_area2_possible = check_area(area2, graph)

    if is_area1_possible and is_area2_possible:

        a1_population = 0
        a2_population = 0

        for area in area1:
            a1_population += populations[area]

        for area in area2:
            a2_population += populations[area]

        diff = abs(a1_population - a2_population)

        if diff < minV:
            minV = diff

if minV == N * 100:
    minV = -1

print(minV)
