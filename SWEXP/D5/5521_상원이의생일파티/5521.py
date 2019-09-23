import sys

sys.stdin = open('sample_input.txt', 'r')

# 상원이(1) 부터 시작해서, 최단 거리가 1 또는 2인 친구들의 수 => 다익스트라

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    D = [N] * (N + 1)  # 최대값은 N?
    D[1] = 0
    adj = [[0] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1
        adj[n2][n1] = 1

    peoples = {i for i in range(1, N + 1)}
    visited = {1}

    for node in peoples - visited:
        w = adj[1][node]
        if w == 1:
            D[node] = 1

    while peoples != visited:
        minV = N
        min_node = None
        for node in peoples - visited:
            if D[node] <= minV:
                minV = D[node]
                min_node = node

        visited = visited | {min_node}

        for i in range(N + 1):
            w = adj[min_node][i]
            if w == 1:
                D[i] = min(D[i], D[min_node] + w)

    cnt = 0
    for i in range(1, N + 1):
        if D[i] in [1, 2]:
            cnt += 1
    print("#{} {}".format(tc, cnt))
