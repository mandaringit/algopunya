import sys

sys.stdin = open('input.txt', 'r')


# 재귀로 풀어보기 ?

def f(n, k, S):
    global cnt
    global numbers

    if n == k:
        if sum(bit) != 0:
            t = 0

            for i in range(k):
                if bit[i] == 1:
                    t += numbers[i]
            if t == S:
                cnt += 1
    else:
        bit[n] = 0
        f(n + 1, k, S)
        bit[n] = 1
        f(n + 1, k, S)


def f2(n, k, S, ts, m):
    global cnt
    if n == k:
        if m > 0 and ts == S:
            cnt += 1
    else:
        f2(n + 1, k, S, ts, m)
        f2(n + 1, k, S, ts + numbers[n], m + 1)


N, S = map(int, input().split())

numbers = list(map(int, input().split()))

bit = [0] * N
cnt = 0
# f(0, N, S)
f2(0, N, S, 0, 0)
print(cnt)
