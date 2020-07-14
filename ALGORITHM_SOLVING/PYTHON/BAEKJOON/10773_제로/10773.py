import sys

sys.stdin = open('input.txt','r')

stack = []

K = int(input())

for _ in range(K):
    number = int(input())

    if number == 0:
        stack.pop()
    else:
        stack.append(number)


print(sum(stack))