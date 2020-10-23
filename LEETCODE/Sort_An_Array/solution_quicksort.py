def partitioning(arr, p, r):
    std = arr[r]  # 기준원소를 맨 마지막으로 잡았다.
    i = p - 1  # 1구역의 끝
    for j in range(p, r, 1):
        if arr[j] <= std:  # 수가 1구역이면
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # 교환해서 1구역에 포함시키기
        # print("1구역:", arr[p:i + 1], "2구역:", arr[i + 1:j + 1], "3구역:", arr[j + 1:r], "4구역:", arr[r])

    arr[i + 1], arr[r] = arr[r], arr[i + 1]  # 1구역의 마지막에 기준점을 넣어준다.
    return i + 1


def quick_sort(arr, p, r):
    if p < r:
        q = partitioning(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)


nums = [31, 8, 38, 73, 11, 3, 20, 29, 65, 15]
quick_sort(nums, 0, len(nums) - 1)
print(nums)
