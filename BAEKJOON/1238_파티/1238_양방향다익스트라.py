import sys

sys.stdin = open('input.txt', 'r')


# 인수의 생일파티랑 똑같음

def dijkstra(reverse=False):
    global adj
    global N, M, X

    U = {X}  # 시작 지점
    D = [100*N]*(N+1)  # 가중치
    D[X] = 0  # 시작점

    for v in V-U:  # 전체 노드 - 확정한 노드 중에서
        w = adj[v][X] if reverse else adj[X][v]
        if 0 < w < 101:  # 인접시
            D[v] = w

    while U != V:
        minV = 100*N
        minIdx = 0

        for v in V-U:
            if D[v] <= minV:
                minV = D[v]
                minIdx = v

        U = U | {minIdx}

        for i in range(1, N+1):
            w = adj[i][minIdx] if reverse else adj[minIdx][i]
            if 0 < w < 101:
                D[i] = min(D[i], D[minIdx]+w)

    return D


N, M, X = map(int, input().split())  # 노드수, 간선수, 도착지
adj = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    n1, n2, w = map(int, input().split())
    adj[n1][n2] = w

V = {i for i in range(1, N+1)}

D = dijkstra()
D_rev = dijkstra(reverse=True)

D_total = [D[i]+D_rev[i] for i in range(N+1)]
D_final = D_total[1:X]+D_total[X+1:]
print(max(D_final))
