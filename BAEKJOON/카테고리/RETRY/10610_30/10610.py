import sys

sys.stdin = open('input.txt', 'r')

# 런타임 에러..??

def perm(n, k):
    global N
    global numbers

    if n == k:
        if N[0] != '0' and N[-1] == '0':
            number = int(''.join(N))
            numbers.append(number)
    else:
        for i in range(n, k):
            N[n], N[i] = N[i], N[n]
            perm(n + 1, k)
            N[n], N[i] = N[i], N[n]


N = list(input().rstrip())
numbers = []

if '0' not in N:
    print(-1)
else:
    perm(0, len(N))
    if not numbers:
        print(-1)
    else:
        print(max(numbers))

