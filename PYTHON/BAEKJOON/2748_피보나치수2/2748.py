import sys

sys.stdin = open('input.txt', 'r')


def fibonacci(N):
    seq = [1, 1]

    if N >= 2:
        for i in range(2, N):
            seq.append(seq[i - 1] + seq[i - 2])

    return seq[N - 1]


N = int(input())

print(fibonacci(N))
