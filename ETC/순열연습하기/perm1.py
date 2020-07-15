arr = [1, 2, 3, 4, 5]


def perm(n, k):
    global arr
    if n == k:
        print(arr)
    else:
        for i in range(n, k):
            arr[i], arr[n] = arr[n], arr[i]
            perm(n + 1, k)
            arr[i], arr[n] = arr[n], arr[i]


perm(0, len(arr))


