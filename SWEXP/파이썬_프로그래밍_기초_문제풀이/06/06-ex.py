
'''
간단한 계산기

'''

operend1 = int(input("첫 번째 숫자를 입력하세요: "))
operator = input("연산자를 입력하세요 (+, -, *, /): ")
operend2 = int(input("두 번째 숫자를 입력하세요: "))


if operator == '+':
    print("{operend1} {op} {operend2} = {result}".format(operend1=operend1,
                                                                op=operator,
                                                                operend2=operend2,
                                                                result=operend1 + operend2))
elif operator == '-':
    print("{operend1} {op} {operend2} = {result}".format(operend1=operend1, op=operator,
                                                                operend2=operend2,
                                                                result=operend1 - operend2))
elif operator == '/':
    print("{operend1} {op} {operend2} = {result}".format(operend1=operend1, op=operator,
                                                                operend2=operend2,
                                                                result=operend1 / operend2))
elif operator == '*':
    print("{operend1} {op} {operend2} = {result}".format(operend1=operend1,
                                                                op=operator,
                                                                operend2=operend2,
                                                                result=operend1 * operend2))
else :
    print("{op}는 본 프로그램에서 지원하지 않는 연산자 입니다.".format(op=operator))