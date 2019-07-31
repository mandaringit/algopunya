# 중복되는 수는 없다고 가정하는듯 하다
test_case = int(input())

for case_number in range(test_case):

    case = [int(num) for num in input().split()]

    case.remove(max(case))
    case.remove(min(case))

    avg = sum(case)/len(case)

    print(f"#{case_number + 1} {round(avg)}")
