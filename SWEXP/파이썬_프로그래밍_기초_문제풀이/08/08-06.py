'''
정렬된 숫자를 가진 리스트에서 특정 숫자를 찾는 함수를 정의하고,

이 함수를 이용해 임의의 숫자의 포함 여부를 출력하는 프로그램을 작성하십시오.

[2, 4, 6, 8, 10]
5 => False
10 => True
'''

sorted_list = [2, 4, 6, 8, 10]

def is_number_in_list(number):
    if number in sorted_list:
        print("%d => True" % number)
    else : print("%d => False" % number)

print(sorted_list)
is_number_in_list(5)
is_number_in_list(10)