'''
소수를 검사하는 함수를 정의하고, 다음의 결과와 같이 사용자가 입력한 숫자가


소수인지를 판단하는 프로그램을 작성하십시오.


소수일 경우 "소수입니다." 출력, 아닐 경우 "소수가 아닙니다." 출력
'''
def number_input() :
    str = input()
    return int(str)

def is_prime_number(number):
    count = 0
    for i in range(1,number+1):
        if number % i ==0 :
            count +=1

    if count == 2 :
        print("소수입니다.")
    else :
        print("소수가 아닙니다.")


is_prime_number(number_input())