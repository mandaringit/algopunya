import sys

sys.stdin = open('s_input.txt', 'r')


def isSimpleIncrease(num):
    snum = str(num)
    for i in range(0, len(snum) - 1):

        if int(snum[i]) > int(snum[i + 1]):
            return False

    return True


def get_max_isi(numbers):
    max_num = -1

    for i in range(N):
        for j in range(i + 1, N):

            mul = numbers[i] * numbers[j]

            if mul > max_num and isSimpleIncrease(mul):
                max_num = mul

    return max_num


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    print("#{} {}".format(t, get_max_isi(numbers)))
