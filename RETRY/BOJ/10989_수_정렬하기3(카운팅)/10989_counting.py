import sys

sys.stdin = open('input.txt', 'r')


def counting_sort(A, N):
    B = [0] * (len(A) + 1)
    counting = [0] * (max(A) + 1)

    for i in range(0, N):
        counting[A[i]] += 1

    for i in range(1, max(A) + 1):
        counting[i] = counting[i] + counting[i - 1]

    for j in range(N - 1, -1, -1):
        B[counting[A[j]]] = A[j]
        counting[A[j]] -= 1

    return B


N = int(input())

numbers = [int(input()) for _ in range(N)]

sorted_numbers = counting_sort(numbers, N)

for i in range(1, N + 1):
    print(sorted_numbers[i])
