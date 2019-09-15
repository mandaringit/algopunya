import sys

sys.stdin = open('input.txt', 'r')


def heapify(arr, k, N):
    left = 2 * k
    right = 2 * k + 1

    if right <= N:  # 오른쪽이 유효한 노드인가? => 자식이 두개인가 ?

        if arr[left] < arr[right]:
            smaller = left
        else:
            smaller = right

    elif left <= N:  # 왼쪽 자식만 있다면

        smaller = left

    else:
        return

    if arr[smaller] < arr[k]:
        arr[k], arr[smaller] = arr[smaller], arr[k]
        heapify(arr, smaller, N)  # 자식노드까지 다시 재귀적으로 살핀다


def build_heap(arr, N):
    for i in range(N // 2, 0, -1):  # N//2 부터 1까지
        heapify(arr, i, N)

    return arr


def heap_sort(arr, N):
    build_heap(arr, N)

    for i in range(N, 1, -1):
        arr[1], arr[i] = arr[i], arr[1]  # 메모리 낭비를 줄이기 위해 자리만 교환
        heapify(arr, 1, i - 1)  # i - 1 을 함으로써 끝부분을 신경쓰지 않게된다.

    return arr


N = int(input())

numbers = [int(sys.stdin.readline()) for _ in range(N)]

numbers = [0] + numbers

heap_sort(numbers, N)  # 역방향으로 정렬되어 있다.

for i in range(N, 0, -1):
    print(numbers[i])
