import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

result = ''
for num in range(1, N + 1):

    snum = str(num)

    if '3' in snum or '6' in snum or '9' in snum:
        count = 0
        for char in snum:
            if char == '3' or char == '6' or char == '9':
                count += 1
        result += f"{'-' * count} "

    else:
        result += f"{snum} "

print(result)
