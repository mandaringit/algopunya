''' #1 축소판
for loop_number in range(int(input())):
    print(f"#{loop_number+1} {max([int(number) for number in input().split()])}")
'''

# 2
case_number = int(input())

result = []

for loop_number in range(case_number):
    case_list = [int(number) for number in input().split()]
    result.append(max(case_list))

for idx, ans in enumerate(result):
    print(f"#{idx+1} {ans}")
