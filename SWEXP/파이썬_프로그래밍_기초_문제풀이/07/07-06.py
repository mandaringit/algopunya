'''
다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.

['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.

출력
{'A': 3, 'O': 3, 'B': 2, 'AB': 2}
'''

bloodTypeList = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

countType = {}

for type in bloodTypeList:
    if type in countType :
        countType[type] +=1
    else :
        countType[type] =1

print(countType)