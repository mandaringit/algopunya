# 시간초과
def apart(a, b):
    if a == 0:
        # 0층 b호엔 b명이 산다
        return b
    else:
        result = 0
        for i in range(1, b+1):
            result += apart(a-1, i)
        return result


T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    print(apart(k, n))

"""
# 재귀 ?
# apart(2,3) = apart(1,1) + apart(1,2) + apart(1,3) + apart(0,1) + apart(0,2) + apart(0,3)
#            = apart(0,1) + [apart(0,1) + apart(0,2)] + [apart(0,1) + apart(0,2) + apart(0,3)] 
#            = 1 + [1+2] + [1+2+3]
#            = 10

def apart(a,b):
    if a == 0:
        # 0층 b호엔 b명이 산다
        return b
    else:
        result = 0
        for i in range(1,b+1):
            result += apart(a-1,i)
        return result

apart(2,3)
"""
