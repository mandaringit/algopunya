import sys

sys.stdin = open('input.txt', 'r')


def the_largest(arr, last):
    largest = last
    for i in range(0, last + 1):
        if arr[i] > arr[largest]:
            largest = i

    return largest


def selection_sort(arr, n):  # 정렬할 배열, 개수
    for last in range(n - 1, 0, -1):  # 처음엔 n-1까지, 한번정렬 후 n-2까지, ..

        # arr[1..last] 중 가장 큰 수 arr[k]를 찾는다.
        k = the_largest(arr, last)
        # 두 값을 교환한다
        arr[last], arr[k] = arr[k], arr[last]

    return arr


N = int(input())

numbers = [int(input()) for _ in range(N)]

selection_sort(numbers, len(numbers))

for num in numbers:
    print(num)
