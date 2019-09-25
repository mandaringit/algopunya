for tc in range(1, 11):
    dump_limit = int(input())

    boxes = list(map(int, input().split()))

    dumping = 0

    while dumping < dump_limit:
        high_boxIdx = boxes.index(max(boxes))
        low_boxIdx = boxes.index(min(boxes))

        boxes[high_boxIdx] -= 1
        boxes[low_boxIdx] += 1

        # 덤핑 횟수 증가
        dumping += 1

    high_box = max(boxes)
    low_box = min(boxes)

    print(f"#{tc} {high_box - low_box}")


"""
import sys

sys.stdin = open("input.txt", 'r')


def get_high_low_idx(box_length, boxes):
    h_box = 0
    h_box_idx = 0
    l_box = 100
    l_box_idx = 0

    for i in range(0, box_length):
        if boxes[i] > h_box:
            h_box = boxes[i]
            h_box_idx = i

        if boxes[i] < l_box:
            l_box = boxes[i]
            l_box_idx = i

    return h_box_idx, l_box_idx


for tc in range(1, 11):
    dump_limit = int(input())

    boxes = list(map(int, input().split()))
    N = len(boxes)
    dumping = 0

    while dumping < dump_limit:
        # 일단 가장 큰 수 / 작은 수와 각각의 인덱스를 구하면 끝
        high_box_idx, low_box_idx = get_high_low_idx(N, boxes)

        boxes[high_box_idx] -= 1
        boxes[low_box_idx] += 1

        # 덤핑 횟수 증가
        dumping += 1

    final_high_box_idx, final_low_box_idx = get_high_low_idx(N, boxes)

    print(f"#{tc} {boxes[final_high_box_idx] - boxes[final_low_box_idx]}")
"""
