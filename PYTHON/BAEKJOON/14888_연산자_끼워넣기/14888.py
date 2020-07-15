# 입력 : N개의 수, N-1개의 연산자들
# 출력 : 수는 그대로 두고, 연산자들의 조합으로 나올 수 있는 최댓값과 최솟값을 출력
# 접근 : 브루트포스 - 모든 연산자들의 조합을 만들어계산 후 비교해보자 3732ms
# 또다른 접근 ?

import sys

sys.stdin = open('input.txt', 'r')


def perm(n, k):
    global ops_permutations
    global ops

    if n == k:
        ops_permutations.append(ops[:])
    else:
        for i in range(n, k):
            ops[n], ops[i] = ops[i], ops[n]
            perm(n + 1, k)
            ops[n], ops[i] = ops[i], ops[n]


N = int(input())
numbers = list(map(int, input().split()))
op_count = list(map(int, input().split()))
ops = []
for i in range(4):
    for k in range(op_count[i]):
        if i == 0:
            ops += ['+']
        elif i == 1:
            ops += ['-']
        elif i == 2:
            ops += ['*']
        elif i == 3:
            ops += ['/']

ops_permutations = []  # 가능한 연산자의 모든 순서
perm(0, N - 1)

minV = 1000000000
maxV = -1000000000

for operators in ops_permutations:
    total = numbers[0]
    for i in range(N - 1):
        op = operators[i]
        number = numbers[i + 1]

        if op == '+':
            total += number
        elif op == '-':
            total -= number
        elif op == '/':
            if total < 0:
                total = -total
                total //= number
                total = -total
            else:
                total //= number
        elif op == '*':
            total *= number

    if total > maxV:
        maxV = total

    if total < minV:
        minV = total

print(maxV)
print(minV)
