import sys

sys.stdin = open('input.txt', 'r')


# 상호배타집합을 구해서 대표값과 자신의 값이 같은것만 고르면...!

def rep(n):
    global p
    while p[n] != n:
        n = p[n]
    return n


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    p = [i for i in range(N + 1)]

    for _ in range(M):
        n1, n2 = map(int, input().split())

        p[rep(n1)] = rep(n2)

    cnt = 0
    for i in range(1, N + 1):
        if i == p[i]:
            cnt += 1

    print("#{} {}".format(tc, cnt))
