'''
다음과 같이 정수 N을 입력받아서 1부터 N까지의 정수를 키로 하고,

그 정수의 제곱을 값으로 하는 딕셔너리 객체를 만드는 코드를 작성하십시오.
'''

input_number = int(input())

pow_dict = {num:pow(num,2) for num in range(1,input_number+1)}

print(pow_dict)
