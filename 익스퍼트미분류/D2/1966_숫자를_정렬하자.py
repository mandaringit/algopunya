test_case = int(input())

for case_number in range(test_case):
    case_length = int(input())
    case = input()

    number_list = sorted([int(num) for num in case.split()])
    print(f"#{case_number+1} {' '.join(list(map(str,number_list)))}")
