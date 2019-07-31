test_case_number = int(input())

result = ""

for loop_number in range(test_case_number):
    input_case = input()
    test_case = [int(number) for number in input_case.split(" ")]

    # 내부에서 바로 해당 테스트케이스에 대해서 계산
    total = sum(test_case)
    avg = round(total/len(test_case))
    if loop_number+1 == test_case_number:
        result += f"#{loop_number+1} {avg}"
    else:
        result += f"#{loop_number+1} {avg}\n"

print(result)
