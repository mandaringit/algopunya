""" #1
# 입력 분리
test_case_number = int(input())

test_cases = []

for number in range(test_case_number):
    input_testcase = [int(number) for number in input().split(" ")]
    test_cases.append(input_testcase)

# print(test_cases)

for idx,case in enumerate(test_cases):
    odd_sum = 0
    for number in case:
        if number % 2:
            odd_sum += number
    print(f"#{idx+1} {odd_sum}")
"""
# 2
# 입력 분리
# 위 풀이 축약
test_case_number = int(input())

result = ""

for number in range(test_case_number):
    input_testcase = [int(number) for number in input().split(" ")]

    odd_sum = 0
    for tc_number in input_testcase:
        if tc_number % 2:
            odd_sum += tc_number

    if number+1 == test_case_number:
        result += f"#{number+1} {odd_sum}"
    else:
        result += f"#{number+1} {odd_sum}\n"

print(result)
