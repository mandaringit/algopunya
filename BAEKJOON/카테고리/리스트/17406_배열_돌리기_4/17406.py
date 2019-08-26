import sys

sys.stdin = open('input.txt', 'r')

def circle_around(i,j,arr,length):

    lines = []

    dIdx = 0

    d = [(1,0),(0,1),(-1,0),(0,-1)]



N, M, K = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]

operators = []

for _ in range(K):
    r, c, s = map(int, input().split())

    l_t = [r - s, c - s]
    r_b = [r + s, c + s]

    center = ((r_b[0] + l_t[0]) // 2, (r_b[1] + l_t[1]) // 2)  # 중점
    length = 2 * s  # 한 변의 길이

    # 홀수일때
    if length % 2:
        # l_t <=   < center   +1 +1씩 옮긴다.

    # 짝수일때
    else:
        # l_t <=   <= center


    operators.append((r, c, s))

print(array, operators)
