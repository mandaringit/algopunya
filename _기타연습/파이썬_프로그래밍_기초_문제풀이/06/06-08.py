# 100~300 사이의 숫자에서 각각의 자리 숫자가 짝수인 숫자를 찾아 콤마(,)로 구분해 출력하는 프로그램을 작성하십시오.

result = ''
isFirst = True

for i in range(100,301):
    strNum = str(i)
    if int(strNum[0]) % 2 == 0 and int(strNum[1]) % 2 == 0 and int(strNum[2]) % 2 == 0 :
        if isFirst:
            result += strNum
            isFirst = False
        else : result += ("," + strNum)

print(result)