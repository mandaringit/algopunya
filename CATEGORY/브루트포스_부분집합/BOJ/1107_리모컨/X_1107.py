# 입력 : 이동하려는 채널 N, 고장난 버튼 수: M , 고장난 버튼들
# 출력 : 채널 N으로 이동 가능할때 까지 누르는 최소 버튼 수
# 시작 채널은 100이고, 최소 차이를 구하면 될거같은데... 그 경우의 수가..?

import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
M = int(input())

total_buttons = set(str(i) for i in range(0, 10))
broken_buttons = set(input().split())
