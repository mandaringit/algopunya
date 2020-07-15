import sys

sys.stdin = open('sample_input.txt', 'r')


def rep(n):
    global p
    while p[n] != n:
        n = p[n]
    return n


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2])  # 가중치 순으로 정렬

    p = [i for i in range(V + 1)]

    total_weight = 0
    N = 0
    for edge in edges:
        n1, n2, weight = edge
        represent1 = rep(n1)
        represent2 = rep(n2)
        if represent1 != represent2:  # 아직까진 서로 상호배타집합일때 (사이클이 아닌경우)
            total_weight += weight
            p[represent1] = represent2
            N += 1
            if N == V:  # 0 부터 V까지 이므로 간선 수는 V + 1 - 1
                break

    print("#{} {}".format(tc, total_weight))
