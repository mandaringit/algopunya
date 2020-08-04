'''
다음의 결과와 같이 피보나치 수열의 결과를 생성하는 프로그램을 작성하십시오.

[입력] 10

[출력] [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
'''

fibonacci_length = int(input())

def get_fibonacci(length):
    fibonacci = [1,1]
    i = 0
    while i <length-2:
        fibonacci.append(fibonacci[i] + fibonacci[i+1])
        i += 1
    print(fibonacci)

get_fibonacci(fibonacci_length)


