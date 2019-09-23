import sys

sys.stdin = open('input.txt', 'r')


# 상호배타집합을 사용한다

def rep(n):
    global p
    while p[n] != n:
        n = p[n]
    return n


N, M = map(int, input().split())
p = [i for i in range(N + 1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    p[rep(n1)] = rep(n2)

cnt = 0
for i in range(1, N + 1):
    if i == p[i]:
        cnt += 1

print(cnt)
