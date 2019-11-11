import sys

sys.stdin = open('input.txt', 'r')


def merge(arr, start, middle, end):
    i = start
    j = middle + 1
    t = 0
    tmp = [0] * (end + 1)

    while i <= middle and j <= end:
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            t += 1
            i += 1
        else:
            tmp[t] = arr[j]
            t += 1
            j += 1

    while i <= middle:
        tmp[t] = arr[i]
        t += 1
        i += 1

    while j <= end:
        tmp[t] = arr[j]
        t += 1
        j += 1

    i = start
    t = 0
    while i <= end:
        arr[i] = tmp[t]
        i += 1
        t += 1


def merge_sort(arr, start, end):  # arr[p ... r] 을 정렬한다.

    if start < end:
        middle = (start + end) // 2  # 중간지점 계산

        merge_sort(arr, start, middle)  # 전반부 정렬
        merge_sort(arr, middle + 1, end)  # 후반부 정렬

        merge(arr, start, middle, end)

    return arr


N = int(input())

numbers = [int(input()) for _ in range(N)]

merge_sort(numbers, 0, len(numbers) - 1)

for num in numbers:
    print(num)
