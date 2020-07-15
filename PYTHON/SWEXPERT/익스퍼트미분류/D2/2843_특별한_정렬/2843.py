import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    numbers = sorted(list(map(int, input().split())))

    f = 0
    b = -1

    sequence = []

    for i in range(10):

        if i % 2:
            # 작은거
            sequence.append(numbers[f])
            f += 1
        else:
            sequence.append(numbers[b])
            b -= 1

    print("#{} {}".format(tc, ' '.join(map(str, sequence))))
