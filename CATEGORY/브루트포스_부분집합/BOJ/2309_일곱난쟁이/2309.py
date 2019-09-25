# 입력 : 9개의 줄에 걸쳐 난쟁이의 키가 주어짐
# 출력 : 7개를 더해서 100이 나오는 경우를 오름차순 정렬해 출력
# 접근 : 기본적으로는 9개중 7개로 만들 수 있는 부분집합을 모두 구해 비교한다.

import sys

sys.stdin = open('input.txt', 'r')

smallers = [int(input()) for _ in range(9)]

for i in range(1, 1 << 9):
    subset = []
    for j in range(9):
        if i & (1 << j):
            subset += [smallers[j]]

    if len(subset) == 7 and sum(subset) == 100:
        subset.sort()
        for tall in subset:
            print(tall)
        break
