T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    blocks = list(map(int, input().split()))

    max_up = 0
    max_down = 0

    for i in range(0, N - 1):
        block1 = blocks[i]
        block2 = blocks[i + 1]

        # 올라가기
        if block1 < block2:
            gap = block2 - block1
            if max_up < gap:
                max_up = gap

        # 내려가기
        if block1 > block2:
            gap = block1 - block2
            if max_down < gap:
                max_down = gap

    print(max_up, max_down)
