import sys

sys.stdin = open('input.txt', 'r')


def bubble_sort(arr, n):
    for last in range(n - 1, 0, -1):  # 맨뒤에서부터, 하나씩 줄여나간다. (정렬된부분제외)

        for i in range(0, last):

            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


def bubble_sort_ver2(arr, n):
    for last in range(n - 1, 0, -1):  # 맨뒤에서부터, 하나씩 줄여나간다. (정렬된부분제외)

        is_sorted = True
        for i in range(0, last):

            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

        if is_sorted:  # 이미 정렬되있는 경우 바로 끝낸다.
            return arr

    return arr


N = int(input())

numbers = [int(input()) for _ in range(N)]

bubble_sort_ver2(numbers, len(numbers))

for num in numbers:
    print(num)
