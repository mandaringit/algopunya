# 입력 : N개의 줄에 해당 상담을 했을때 걸리는 시간 및 보상들
# 출력 : N+1일에 퇴사 전까지 일해서 얻을 수 있는 가장 큰 수익
# 접근1. 모든 부분집합 -> 가능 여부 -> 계산해 구하기
# 접근2. DP적인 접근 . i일의 dp값 = 이날 상담이 '가능'하다면 해당 일의 보상 (못하면 0) + max(i일 이전까지의 상담들 중 i-1일에 상담이 완료된 것들의 dp값)

import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
dp = [0] * (N + 1)
days = [0] * (N + 1)
for i in range(1, N + 1):
    T, P = map(int, input().split())
    end_day = i + T - 1
    days[i] = (end_day, P)  # 종료일을 구해서 저장하자

for i in range(1, N + 1):

    dp[i] = days[i][1] if days[i][0] <= N else 0  # 1. 해당 일자의 상담이 가능하면 그 상담으로 얻을 보상 or 0

    max_dp = 0  # 2. i일 이전까지의 상담들 중 i-1일에 상담이 완료된 것들의 dp값의 최대를 찾자.
    for j in range(1, i):
        compare_day = days[j][0]
        compare_dp = dp[j]
        if compare_day < i and compare_dp > max_dp:
            max_dp = dp[j]

    dp[i] += max_dp  # 1 + 2 가 그날의 dp값

print(max(dp))
