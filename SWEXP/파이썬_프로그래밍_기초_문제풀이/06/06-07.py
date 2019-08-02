'''
1~200 사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌 모든 숫자들을 찾아

콤마(,)로 구분된 문자열을 구성해 출력하는 프로그램을 작성하십시오.
'''
result = ''
isFirst = True

for i in range(1,201):
    if i%7 == 0 and i%5 !=0 :
        if isFirst == True:
            result += '%s' % i
            isFirst = False
        else:
            result += ',%s' % i


print(result)