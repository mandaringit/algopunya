import sys

sys.stdin = open('input.txt', 'r')


def prim(start):
    global adj
    global islands
    global N
    global min_cost_limit

    visited_islands = {start}
    possible_islands = set(k for k in range(N)) - visited_islands
    total_cost = 0

    while possible_islands:
        min_cost = min_cost_limit
        min_land = None
        for v_land in visited_islands:
            for p_land in possible_islands:
                cost = adj[v_land][p_land]
                if cost < min_cost:
                    min_cost = cost
                    min_land = p_land

        total_cost += min_cost
        visited_islands.add(min_land)
        possible_islands -= {min_land}

    return round(total_cost)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    x_coords = list(map(int, input().split()))
    y_coords = list(map(int, input().split()))
    islands = list(zip(x_coords, y_coords))
    E = float(input())

    adj = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(i + 1, N):
            land1 = islands[i]
            land2 = islands[j]
            distance = (land1[0] - land2[0]) ** 2 + (land1[1] - land2[1]) ** 2  # 각 섬들의 거리

            adj[i][j] = E * distance
            adj[j][i] = E * distance
    min_cost_limit = pow(1000000, 2) * 2
    print("#{} {}".format(tc,prim(0)))
