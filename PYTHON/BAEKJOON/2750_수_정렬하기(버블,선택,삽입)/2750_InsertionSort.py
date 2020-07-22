import sys

sys.stdin = open('input.txt')


def insertion_sort(arr, N):
    for i in range(1, N):
        idx = i
        while arr[idx] < arr[idx - 1] and idx > 0:
            arr[idx], arr[idx - 1] = arr[idx - 1], arr[idx]
            idx -= 1
    return arr


N = int(input())
arr = [int(input()) for _ in range(N)]
for v in insertion_sort(arr, N):
    print(v)
