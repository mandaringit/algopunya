import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

weights = [int(input()) for _ in range(N)]

weights.sort()  # 크기순으로 정렬하고,

allowed = []

for i in range(N):
    k = N - i

    allowed_weight = weights[i] * k  # 해당 로프를 선택했을때, 가용 무게는 자신과 같거나 큰거 개수 * 자신의 무게

    allowed.append(allowed_weight)

print(max(allowed))
