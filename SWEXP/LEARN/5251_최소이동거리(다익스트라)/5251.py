import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split())

    # 인접행렬 생성
    adj = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w  # s -> e 로 가는 가중치

    V = {i for i in range(N + 1)}
    U = {0}  # 선택된 정점집합. 시작부분 포함하기

    D = [0] * (N + 1)  # 거리들

    for v in V - U:
        weight = adj[0][v]
        if weight == 0:  # 못가는곳
            D[v] = 11  # 될 수 있는한 최대(무한대개념)
        else:
            D[v] = weight

    while U != V:
        # 안고른 노드들 중, 최소를 찾는다.
        w = None
        minimum_w = 11
        for node in V - U:
            if D[node] <= minimum_w:
                w = node
                minimum_w = D[node]

        U = U | {w}  # 최소 노드 포함

        for i in range(N + 1):
            v = adj[w][i]  # 인접 정점의 가중치
            if 0 < v < 11:  # 인접하면,
                D[i] = min(D[i], D[w] + v)  # 비교
    print(D)
    print("#{} {}".format(tc, D[N]))
