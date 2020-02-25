import sys

sys.stdin = open('sample_input.txt', 'r')


def insertion(x):
    global heap, tail
    tail += 1
    heap[tail] = x
    next_idx = tail
    while 1 <= next_idx // 2 and heap[next_idx // 2] < heap[next_idx]:
        heap[next_idx // 2], heap[next_idx] = heap[next_idx], heap[next_idx // 2]
        next_idx //= 2


def extract_max():
    global heap, tail, extracted
    if heap[1] > 0:
        heap[1], heap[tail] = heap[tail], heap[1]  # 자리교환
        temp_idx = 1
        while temp_idx < tail // 2:
            left = temp_idx * 2
            right = temp_idx * 2 + 1

            if heap[left] >= heap[right]:
                heap[temp_idx], heap[left] = heap[left], heap[temp_idx]
                temp_idx = left
            else:
                heap[temp_idx], heap[right] = heap[right], heap[temp_idx]
                temp_idx = right

        extracted.append(heap[tail])
        heap[tail] = 0
        tail -= 1
    else:
        extracted.append(-1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    heap = [0] * (N + 1)
    tail = 0
    extracted = []
    for _ in range(N):
        cmd = list(map(int, input().split()))

        # 추가
        if cmd[0] == 1:
            insertion(cmd[1])
        # 삭제
        else:
            extract_max()

    print(f"#{tc} {' '.join(map(str, extracted))}")
