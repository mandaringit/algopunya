def merge(arr, p, q, r):
    i = p
    j = q + 1
    t = 0
    temp = [0 for i in range(r + 1)]
    # 왼쪽이 끝까지 또는 오른쪽이 끝까지 갈때까지
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            temp[t] = arr[i]
            i += 1
        else:
            temp[t] = arr[j]
            j += 1
        t += 1
    while i <= q:
        temp[t] = arr[i]
        i += 1
        t += 1
    while j <= r:
        temp[t] = arr[j]
        j += 1
        t += 1

    i = p
    t = 0
    while i <= r:
        arr[i] = temp[t]
        i += 1
        t += 1


def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)

    return arr


N = int(input())
arr = [int(input()) for _ in range(N)]
for v in merge_sort(arr, 0, N - 1):
    print(v)
