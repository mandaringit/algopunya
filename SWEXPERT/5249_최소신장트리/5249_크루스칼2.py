import sys

sys.stdin = open('sample_input.txt', 'r')


def rep(n):
    global p
    while n != p[n]:
        n = p[n]
    return n


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    G = {i: set() for i in range(V + 1)}
    # 간선을 모은다
    edges = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edges.append([n1, n2, w])
        G[n1].add(n2)

    # 간선을 작은순으로 오름차순 정렬한다.
    edges.sort(key=lambda x: x[2])

    p = [i for i in range(V + 1)]  # 대표원소들의 집합
    T = []  # 신장 트리 가중치 모음
    while len(T) < V:
        n1, n2, w = edges.pop(0)

        represent1 = rep(n1)  # n1의 대표원소
        represent2 = rep(n2)  # n2의 대표원소

        if represent1 != represent2:  # 대표원소가 동일하지 않다 -> 사이클이 아니다.
            T.append(w)  # 신장트리에 추가하고
            p[represent2] = represent1  # 대표원소 통일

    print(sum(T))
