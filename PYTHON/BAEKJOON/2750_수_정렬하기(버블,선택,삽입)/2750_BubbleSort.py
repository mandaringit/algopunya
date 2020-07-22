def bubble_sort(arr, N):
    for i in range(N - 1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


N = int(input())
arr = [int(input()) for _ in range(N)]
for v in bubble_sort(arr, N):
    print(v)
