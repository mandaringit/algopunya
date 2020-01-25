import sys

sys.stdin = open('input.txt', 'r')

numbers = list(map(int, input().split()))
square_numbers = [x ** 2 for x in numbers]
print(sum(square_numbers) % 10)
