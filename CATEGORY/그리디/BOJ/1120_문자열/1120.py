import sys

sys.stdin = open('input.txt', 'r')

A, B = input().split()
N = len(A)
min_diff = 50
# 앞에서 비교
for i in range(0, len(B) - N + 1):
    diff = 0
    word = B[i:i + N]
    for i in range(len(A)):
        if word[i] != A[i]:
            diff += 1
            if diff > min_diff:
                break

    if diff < min_diff:
        min_diff = diff

print(min_diff)
