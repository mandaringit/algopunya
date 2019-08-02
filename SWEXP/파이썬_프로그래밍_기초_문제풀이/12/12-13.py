'''
다음의 결과와 같이 사용자로부터 콤마(,)로 구분해 여러 원의 반지름을 입력 받아

이들에 대한 원의 둘레를 계산해 출력하는 프로그램을 작성하십시오.
'''

numbers = input()

split_numbers = numbers.split(",")
PI = 3.141592
radiuses = [int(number.strip())*2*PI for number in split_numbers]

result = ''

for idx,radius in enumerate(radiuses):
    if idx == len(radiuses)-1:
        result+="{0:0.2f}".format(radius)
    else :
        result += "{0:0.2f}, ".format(radius)

print(result)