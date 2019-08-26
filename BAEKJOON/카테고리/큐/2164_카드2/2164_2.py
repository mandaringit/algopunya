# 모듈 안쓰고 해보기
import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

cards = [num for num in range(1, N + 1)]
front = 0
back = len(cards) - 1

while front != back:
    cards[front] = 0
    front += 1
    cards.append(cards[front])
    back += 1
    cards[front] = 0
    front += 1

print(cards[-1])
