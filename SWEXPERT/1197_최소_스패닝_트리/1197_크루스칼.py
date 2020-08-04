import sys

sys.stdin = open('input.txt', 'r')

# 통과

def rep(n):
    global p
    while p[n] != n:
        n = p[n]

    return n


V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])
p = [i for i in range(10001)]

cnt = 0
total_weight = 0
for edge in edges:
    n1, n2, w = edge
    represent1 = rep(n1)
    represent2 = rep(n2)
    if represent1 != represent2:
        p[represent1] = represent2
        total_weight += w
        cnt += 1

        if cnt == V - 1:
            break
print(total_weight)
