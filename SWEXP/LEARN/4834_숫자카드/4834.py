import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())

    card_box = [0]*10

    cards = input()

    for i in range(0, N):
        number = int(cards[i])
        card_box[number] = card_box[number] + 1

    max_number = 0
    max_count = 0

    for i in range(0, 10):
        if card_box[i] >= max_count:
            max_count = card_box[i]
            max_number = i

    print(f"#{t} {max_number} {max_count}")


