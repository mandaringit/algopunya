'''
다음은 학생의 점수를 나타내는 리스트입니다.

[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]

while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.
'''

scoreList = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]

listLen = len(scoreList)
sum = 0

while listLen > 0 :
    if scoreList[listLen-1] >= 80:
        sum += scoreList[listLen-1]
    scoreList.pop()
    listLen = len(scoreList)

print(sum)