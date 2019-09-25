import sys

sys.stdin = open('sample_input.txt', 'r')


def is_run(cards):
    return cards.count(3) > 0


def is_triplet(cards):
    for i in range(8):
        if cards[i:i + 3].count(0) == 0:
            return True

    return False


T = int(input())

for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))

    odd_counting = [0] * 10
    even_counting = [0] * 10

    winner = 0

    for i in range(len(numbers)):

        # 카드 분배
        if i % 2 == 0:  # 여기선 홀수
            odd_counting[numbers[i]] += 1
            run1 = is_run(odd_counting)
            tri1 = is_triplet(odd_counting)

            if run1 or tri1:
                if winner == 0:
                    winner = 1
        else:
            even_counting[numbers[i]] += 1
            run2 = is_run(even_counting)
            tri2 = is_triplet(even_counting)
            if run2 or tri2:
                if winner == 0:
                    winner = 2

    print("#{} {}".format(tc, winner))
