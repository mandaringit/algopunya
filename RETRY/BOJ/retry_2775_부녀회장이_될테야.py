# 뭐가틀린거야 ㅅㅂ
def memoize(func):
    memo = {}

    def wrapped(k, n):
        if f"{k}{n}" in memo:
            return memo[f"{k}{n}"]
        else:
            result = func(k, n)
            memo[f"{k}{n}"] = result
#             print(memo)
            return result
    return wrapped


@memoize
def apart(k, n):
    if k == 0:
        # 0층 b호엔 b명이 산다
        return n
    else:
        result = 0
        for i in range(1, n+1):
            result += apart(k-1, i)
        return result


T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    print(apart(k, n))

"""
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
"""
# 재귀 ?
# apart(2,3) = apart(1,1) + apart(1,2) + apart(1,3) 
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
