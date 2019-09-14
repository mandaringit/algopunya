import sys

sys.stdin = open('input.txt', 'r')


def insertion_sort(arr, n):
    for i in range(1, n):
        # arr[1..i]의 적합한 자리에 a[i]를 삽입한다.

        loc = i - 1
        new_item = arr[i]  # 비교 대상
        # 이지점에서 arr[1 .. i-1]은 이미 정렬된상태

        while loc >= 0 and new_item < arr[loc]:  # 왼쪽과 비교하면서, 비교대상이 해당 원소보다 작을동안 돈다
            arr[loc + 1] = arr[loc]  # 한칸씩 옆으로 미는 작업
            loc -= 1  # 위치 감소

        arr[loc + 1] = new_item  # 자기자리에 와서 비교대상으로 변경


N = int(input())

numbers = [int(input()) for _ in range(N)]

insertion_sort(numbers, len(numbers))

for num in numbers:
    print(num)
