import sys

sys.stdin = open('input.txt', 'r')

names = input().split('-')
shorten = ''
for name in names:
    shorten += name[0]

print(shorten)
