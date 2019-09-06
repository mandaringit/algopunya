import sys

sys.stdin = open('sample_input.txt', 'r')


def get_hex(numbers, N):
    possible_hex = set()
    for i in range(0, N, N // 4):
        possible_hex.add(''.join(numbers[i:i + N // 4]))

    return possible_hex


T = int(input())

for tc in range(1, T + 1):
    # N개의 숫자, 내림차순정렬 했을때 K번째 숫자를 구하자.
    N, K = map(int, input().split())

    numbers = list(input())

    possible_hex = get_hex(numbers, N)

    for i in range(N // 4 - 1):
        num = numbers.pop()
        numbers.insert(0, num)
        possible_hex.update(get_hex(numbers, N))

    possible_hex = sorted(list(map(lambda x: int(x, 16), possible_hex)), reverse=True)
    print("#{} {}".format(tc, possible_hex[K - 1]))
