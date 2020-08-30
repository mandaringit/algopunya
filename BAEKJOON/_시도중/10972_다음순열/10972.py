import sys

sys.stdin = open('input.txt', 'r')


# 런타임에러?

def perm(n, k):
    global numbers
    global cases
    if n == k:
        cases.append(int(''.join(map(str, numbers[:]))))
    else:
        for i in range(n, k):
            numbers[n], numbers[i] = numbers[i], numbers[n]
            perm(n + 1, k)
            numbers[n], numbers[i] = numbers[i], numbers[n]


N = int(input())
target = input().split()
numbers = [i for i in range(1, N + 1)]
cases = []
perm(0, N)
cases.sort()
idx = cases.index(int(''.join(target)))
if idx == len(cases) - 1:
    print(-1)
else:
    print(' '.join(list(str(cases[idx + 1]))))
