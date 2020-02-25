import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())  # N장의 카드가 주어진다.
    num = input()  # 카드들
    cards = [0]*10  # 0-9 까지 자리를 만들어준다.

    print("미리 만든 카드함 => ",cards)

    for i in num:
        card_idx = int(i)
        cards[card_idx] = cards[card_idx] + 1

    print("돌면서 쌓인 카드함 => ",cards)
    maxIdx = 0

    # 각자 카드를 돌면서 확인

    for i in range(0,10):
        if cards[maxIdx] <= cards[i]:
            maxIdx = i

    print("#{} {} {}".format(tc, maxIdx, cards[maxIdx]))
