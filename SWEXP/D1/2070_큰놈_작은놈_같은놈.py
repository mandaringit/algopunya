case_number = int(input())

result = ""

for loop_number in range(case_number):
    num1, num2 = input().split()
    ans = f'#{loop_number+1} '
    if num1 > num2:
        ans += '>'
    elif num1 < num2:
        ans += '<'
    else:
        ans += '='

    result += ans
    if loop_number+1 != case_number:
        result += '\n'

print(result)
