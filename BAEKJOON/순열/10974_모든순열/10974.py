import sys

sys.stdin = open('input.txt', 'r')


def perm(n, k):
    global numbers
    global cases

    if n == k:
        cases.append(int("".join(map(str, numbers[:]))))
    else:
        for i in range(n, k):
            numbers[n], numbers[i] = numbers[i], numbers[n]
            perm(n + 1, k)
            numbers[n], numbers[i] = numbers[i], numbers[n]


N = int(input())
numbers = [i for i in range(1, N + 1)]
cases = []
perm(0, N)
cases.sort() # 사전순

for case in cases:
    print(' '.join(str(case)))
