import sys

sys.stdin = open('sample_input.txt', 'r')

'''
0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때,
이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 만드시오.
[입력]
첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 마지막 노드번호 V와 간선의 개수 E가 주어진다.
다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드 n1, n2, 가중치 w가 차례로 주어진다. 
1<=T<=50, 1<=V<=1000, 1<=w<=10, 1<=E<=1000000
'''


# prim 1
def extractMin(Q, d):
    global max_weight
    minD = max_weight
    minU = 0

    for u in Q:
        if d[u] < minD:
            minD = d[u]
            minU = u

    return minU


def prim_ver1(G, r):
    global max_weight
    V_set = set(G.keys())
    S_set = set()  # 정점 집합

    d = [max_weight] * len(V_set)  # 가중치 10이 최대.

    d[r] = 0

    while S_set != V_set:
        u = extractMin(V_set - S_set, d)
        S_set = S_set | {u}

        for v in G[u]:
            if v in V_set - S_set and adj[(u, v)] < d[v]:
                d[v] = adj[(u, v)]

    return d

# prim 2
def deleteMin(Q, d):
    global max_weight
    minD = max_weight
    minU = 0

    for u in Q:
        if d[u] < minD:
            minD = d[u]
            minU = u
    Q.remove(minU)
    return minU


def prim_ver2(G, r):
    global max_weight
    Q = set(G.keys())

    d = [max_weight] * len(Q)

    d[r] = 0

    while len(Q) != 0:
        u = deleteMin(Q, d)
        for v in G[u]:
            if v in Q and adj[(u, v)] < d[v]:
                d[v] = adj[(u, v)]

    return d


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    max_weight = 11
    G = {i: [] for i in range(V + 1)}
    adj = {}
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        G[n1].append(n2)
        G[n2].append(n1)
        adj[(n1, n2)] = w
        adj[(n2, n1)] = w

    d1 = prim_ver1(G, 0)
    d2 = prim_ver2(G, 0)
    print(d1)
    print(d2)
