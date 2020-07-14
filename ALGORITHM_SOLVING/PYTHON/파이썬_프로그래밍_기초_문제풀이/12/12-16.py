'''
콤마(,)로 구분해 숫자를 입력하고, 입력된 숫자 중 홀수를 콤마(,)로 구분해 출력하는

리스트 내포 기능을 이용한 프로그램을 작성하십시오.
'''

numbers = input()

split_numbers = numbers.split(",")

odd_numbers = [int(number.strip()) for number in split_numbers if int(number.strip()) % 2 != 0]

result = ""
for idx,number in enumerate(odd_numbers):
    if idx == len(odd_numbers)-1:
        result += "{}".format(number)
    else:
        result += "{}, ".format(number)

print(result)