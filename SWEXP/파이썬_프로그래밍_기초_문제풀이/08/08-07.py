'''
다음과 같이 팩토리얼을 구하는 함수를 정의해 입력된 숫자에 대한

팩토리얼 값을 구하는 프로그램을 작성하십시오.
'''

fact_number = int(input())

def factorial(number):
    result = 1
    while number > 0 :
        result *= number
        number -= 1

    return result

print(factorial(fact_number))