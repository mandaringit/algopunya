import sys

sys.stdin = open('input.txt', 'r')


def create_number(number, size):
    global align
    global max_size

    width = size
    height = size * 2 - 1
    result = []

    if align == 'BOTTOM':
        padding = 2 * max_size - 1 - height
        for _ in range(padding):
            result.append('.' * width)

    if align == 'MIDDLE':
        half_padding = (2 * max_size - 1 - height) // 2
        for _ in range(half_padding):
            result.append('.' * width)

    if number == '0':
        result.append("#" * size)
        for _ in range(height - 2):
            result.append("#" + "." * (width - 2) + "#")
        result.append("#" * size)
    elif number == '1':
        for _ in range(height):
            result.append("." * (width - 1) + "#")
    elif number == '2':
        result.append("#" * width)
        for _ in range((height - 3) // 2):
            result.append("." * (width - 1) + "#")
        result.append("#" * width)
        for _ in range((height - 3) // 2):
            result.append("#" + "." * (width - 1))
        result.append("#" * width)

    elif number == '3':
        result.append("#" * width)
        for _ in range((height - 3) // 2):
            result.append("." * (width - 1) + "#")
        result.append("#" * width)
        for _ in range((height - 3) // 2):
            result.append("." * (width - 1) + "#")
        result.append("#" * width)

    elif number == '4':
        for _ in range((height - 1) // 2):
            result.append("#" + "." * (width - 2) + "#")
        result.append("#" * width)
        for _ in range((height - 1) // 2):
            result.append("." * (width - 1) + "#")

    elif number == '5':
        result.append("#" * width)
        for _ in range((height - 3) // 2):
            result.append("#" + "." * (width - 1))
        result.append("#" * width)
        for _ in range((height - 3) // 2):
            result.append("." * (width - 1) + "#")
        result.append("#" * width)
    elif number == '6':
        for _ in range((height - 2) // 2 + 1):
            result.append("#" + "." * (width - 1))
        result.append("#" * width)
        for _ in range((height - 2) // 2):
            result.append("#" + "." * (width - 2) + "#")
        result.append("#" * width)
    elif number == '7':
        result.append("#" * width)
        for _ in range(height - 1):
            result.append("." * (width - 1) + "#")
    elif number == '8':
        result.append("#" * width)
        for _ in range((height - 3) // 2):
            result.append("#" + "." * (width - 2) + "#")
        result.append("#" * width)
        for _ in range((height - 3) // 2):
            result.append("#" + "." * (width - 2) + "#")
        result.append("#" * width)
    elif number == '9':
        result.append("#" * width)
        for _ in range((height - 2) // 2):
            result.append("#" + "." * (width - 2) + "#")
        result.append("#" * width)
        for _ in range((height - 2) // 2 + 1):
            result.append("." * (width - 1) + "#")

    if align == 'TOP':
        padding = 2 * max_size - 1 - height
        for _ in range(padding):
            result.append('.' * width)

    if align == 'MIDDLE':
        half_padding = (2 * max_size - 1 - height) // 2
        for _ in range(half_padding):
            result.append('.' * width)

    return result


N, align = input().split()

final = []
print_this = []

max_size = 0
for _ in range(int(N)):
    size, numbers = input().split()
    print_this.append((int(size), numbers))
    if int(size) > max_size:
        max_size = int(size)

for size, numbers in print_this:

    for number in numbers:
        final.append(create_number(number, size))

for i in range(max_size * 2 - 1): # 줄들
    line = []
    for number in final:
        line.append(number[i])

    print(" ".join(line))
