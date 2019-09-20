import sys

sys.stdin = open('input.txt', 'r')

# ?? 가중치가 모두 1인데, ...
# 분기가 모두 하나씩만 나있으면 N-1이 맞지만
# 분기가 두개 이상인개 여러개 있으면 조금 달라지지 않나? 왕복한 거리까지 ?? 왕복은 안세나 ?? 모르겟넹
# MST인지는 의문이 듦

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = {i: set() for i in range(1, N + 1)}

    for _ in range(M):
        node1, node2 = map(int, input().split())

        graph[node1].add(node2)
        graph[node2].add(node1)

    print(N - 1)
