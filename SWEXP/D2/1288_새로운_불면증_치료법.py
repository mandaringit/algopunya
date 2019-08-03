cases = int(input())

for case_number in range(cases):
    N = int(input())

    true_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
    answer_set = set()
    count = 0
    next_num = N

    while answer_set != true_set:
        count += 1
        next_num = N*(count)
        str_N = str(next_num)
        for num in str_N:
            answer_set.add(num)

    print(f"#{case_number + 1} {next_num}")


"""
#테스트 끄적끄적
N = 11

true_set ={'1','2','3','4','5','6','7','8','9','0'}
answer_set = set()
count = 0
next_num = N

while answer_set != true_set:
    count += 1
    next_num = N*(count)
    str_N = str(next_num)
    for num in str_N:
        answer_set.add(num)
    
    
print(next_num)
"""
