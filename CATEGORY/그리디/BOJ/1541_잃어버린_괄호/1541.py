import sys

sys.stdin = open('input.txt', 'r')

equation = input().split('-')  # - 기준으로 나누기

total = 0

for i in range(len(equation)):
    numbers = list(map(int, equation[i].split('+')))

    if i == 0:
        total += sum(numbers)
    else:
        total -= sum(numbers)

print(total)



