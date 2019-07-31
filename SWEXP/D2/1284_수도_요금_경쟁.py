"""
# 테스트 끄적끄적
P,Q,R,S,W = (9,100,20,3,10)

company_A = W * P
if W <= R:
    company_B = Q
else:
    company_B = Q + (W-R)*S

print(min(company_A,company_B))
"""

cases = int(input())
for case_count in range(cases):
    P, Q, R, S, W = tuple(map(int, input().split()))

    com_A = W*P
    com_B = Q if W <= R else Q + (W-R)*S

    print(f"#{case_count+1} {min(com_A,com_B)}")
