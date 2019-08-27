import sys

sys.stdin = open('input.txt', 'r')


def blackjack(N, M, cards):
    max_sum = 0
    for i in range(N):
        for j in range(N):
            if j != i:
                for k in range(N):
                    if k != i and k != j:
                        total = cards[i] + cards[j] + cards[k]
                        if max_sum < total <= M:
                            max_sum = total

                        if max_sum == M:
                            return max_sum
    return max_sum


N, M = map(int, input().split())

cards = list(map(int, input().split()))

print(blackjack(N, M, cards))
