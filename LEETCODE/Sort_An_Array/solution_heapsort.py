# 초기 배열을 heap의 구조로 만드는 과정
def buildHeap(arr):
    heap = [0] + arr
    N = len(arr)
    for i in range(N // 2, 0, -1):  # 리프노드가 아닌 마지막 노드부터 시작.
        heapify(heap, i, N)
    return heap

# k번째 노드를 루트로 하는 트리를 힙성질을 만족하도록 만든다.
# n은 전채 배열의 크기.


def heapify(heap, k, n):
    left = 2 * k
    right = 2 * k + 1
    if right <= n:  # 왼쪽 / 오른쪽 둘다 있을때.
        if heap[left] < heap[right]:
            smaller = left
        else:
            smaller = right
    elif left <= n:  # 왼쪽만 있을때.
        smaller = left
    else:
        return

    if heap[smaller] < heap[k]:
        heap[k], heap[smaller] = heap[smaller], heap[k]
        heapify(heap, smaller, n)  # 바꿔서 힙의 성질이 깨질 수 있으니 수선.

# 정렬은 루트를 뽑아내고, 마지막 노드를 다시 올린 후 힙화를 반복한다.


def heapSort(arr):
    N = len(arr)
    arr = buildHeap(arr)
    sorting = []
    for i in range(N, 0, -1):
        sorting.append(arr[1])  # 항상 맨 처음이 가장 작은수이므로 이를 가져온다.
        arr[1], arr[i] = arr[i], arr[1]  # 맨 마지막 노드와 교환
        heapify(arr, 1, i - 1)  # 맨 마지막을 없앤 효과를 위해 길이를 줄임

    return sorting


heapSort([5, 1, 1, 2, 0, 0])
