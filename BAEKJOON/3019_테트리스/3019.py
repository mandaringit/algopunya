import sys

sys.stdin = open('input.txt', 'r')


# 높이차이에 중점을 두고 보면 단순구현 + 브루트포스

def Block(P):
    global fields
    global C

    count = 0

    if P == 1:
        count += C  # 세로일때

        for i in range(0, C - 4 + 1):
            h = fields[i]
            if fields[i + 1] == h and fields[i + 2] == h and fields[i + 3] == h:
                count += 1

    elif P == 2:
        for i in range(0, C - 2 + 1):
            if fields[i] == fields[i + 1]:
                count += 1

    elif P == 3:
        # original
        for i in range(0, C - 3 + 1):
            h = fields[i]
            if fields[i + 1] == h and fields[i + 2] == h + 1:  # 001
                count += 1

        # r 90
        for i in range(0, C - 2 + 1):
            h = fields[i]
            if fields[i + 1] == h - 1:  # 10
                count += 1

    elif P == 4:
        # original
        for i in range(0, C - 3 + 1):
            h = fields[i]
            if fields[i + 1] == h - 1 and fields[i + 2] == h - 1:  # 100
                count += 1

        # r 90
        for i in range(0, C - 2 + 1):
            h = fields[i]
            if fields[i + 1] == h + 1:  # 01
                count += 1

    elif P == 5:
        # original, r 180
        for i in range(0, C - 3 + 1):
            h = fields[i]

            if fields[i + 1] == h and fields[i + 2] == h:
                count += 1

            if fields[i + 1] == h - 1 and fields[i + 2] == h:  # 101
                count += 1

        # r 90 , 270
        for i in range(0, C - 2 + 1):
            h = fields[i]
            if fields[i + 1] == h + 1:  # 01
                count += 1

            if fields[i + 1] == h - 1:  # 10
                count += 1

    elif P == 6:
        # original, r180
        for i in range(0, C - 3 + 1):
            h = fields[i]

            if fields[i + 1] == h and fields[i + 2] == h:
                count += 1

            if fields[i + 1] == h + 1 and fields[i + 2] == h + 1:  # 011
                count += 1

        # r90 r270
        for i in range(0, C - 2 + 1):
            h = fields[i]

            if fields[i + 1] == h:  # 00
                count += 1

            if fields[i + 1] == h - 2:  # 20
                count += 1

    elif P == 7:
        # original, r180
        for i in range(0, C - 3 + 1):
            h = fields[i]

            if fields[i + 1] == h and fields[i + 2] == h:
                count += 1

            if fields[i + 1] == h and fields[i + 2] == h - 1:  # 110
                count += 1

        # r90 r270
        for i in range(0, C - 2 + 1):
            h = fields[i]

            if fields[i + 1] == h:  # 00
                count += 1

            if fields[i + 1] == h + 2:  # 02
                count += 1

    return count


C, P = map(int, input().split())
fields = list(map(int, input().split()))
print(Block(P))
