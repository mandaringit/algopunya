import sys

sys.stdin = open('sample_input.txt', 'r')


def partition(arr, start, end):
    x = arr[end]  # 여기선 마지막을 기준 원소로 잡는다.

    # 1구역(기준보다 작은) / 2구역(기준보다 큰) / 3구역 (아직 정해지지 않은) / 4구역 (기준원소)

    i = start - 1  # 1구역의 끝지점

    for j in range(start, end):  # j는 3구역의 시작지점
        if arr[j] <= x:
            i += 1  # 1구역 끝지점 늘려주기
            arr[j], arr[i] = arr[i], arr[j]  # 기준원소보다 작으면 해당 자리를 1구역 끝과 교환

    arr[i + 1], arr[end] = arr[end], arr[i + 1]  # 마지막으로 4구역에 남은 '기준원소'를 2구역 첫번째 원소와 교환

    return i + 1


def quick_sort(arr, start, end):
    if start < end:
        q = partition(arr, start, end)  # 분할
        quick_sort(arr, start, q - 1)
        quick_sort(arr, q + 1, end)

    return arr


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    numbers = list(map(int, input().split()))

    quick_sort(numbers, 0, N - 1)

    print("#{} {}".format(tc, numbers[N // 2]))
