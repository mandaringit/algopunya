import sys

sys.stdin = open('input.txt', 'r')


def f(n, k, m):
    global cnt
    if n == k:
        if m == K:
            cnt += 1
    elif m > K:
        return
    else:
        f(n + 1, k, m)
        f(n + 1, k, m + array[n])


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    array = list(map(int, input().split()))
    cnt = 0
    f(0, N, 0)
    print('#{} {}'.format(tc, cnt))
