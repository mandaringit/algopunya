'''
다음의 결과와 같이 어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.

입력

11


출력

0 1 2 3 4 5 6 7 8 9
0 2 0 0 0 0 0 0 0 0

'''

number = input()

numberDic = {}

for i in number :
    if i in numberDic :
        numberDic[i] += 1
    else : numberDic[i] = 1

numberList = ''
numberCount = ''

for i in range(0,10):
    numberList += "%s " % str(i)
    if str(i) in numberDic:
        numberCount += "%s " % str(numberDic[str(i)])
    else :
        numberCount += "0 "


print(numberList.strip())
print(numberCount.strip())