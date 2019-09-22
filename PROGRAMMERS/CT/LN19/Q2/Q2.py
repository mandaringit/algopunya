import sys

sys.stdin = open('input.txt', 'r')


def perm(n, k):
    global numbers
    global cases

    if n == k:
        cases.append(numbers[:])
    else:
        for i in range(n, k):
            numbers[n], numbers[i] = numbers[i], numbers[n]
            perm(n + 1, k)
            numbers[n], numbers[i] = numbers[i], numbers[n]


numbers = list(map(int, input().strip().split()))
N = int(input())
cases = []
perm(0, len(numbers))
print(''.join(map(str, cases[N - 1])))
