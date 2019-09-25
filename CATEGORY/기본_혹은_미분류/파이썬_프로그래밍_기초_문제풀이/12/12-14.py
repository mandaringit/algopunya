'''
다음과 같이 2차원 배열 구조를 만들기 위한 행, 열 정보를 콤마(,)로 구분해 입력하고,

이 리스트 객체의 항목의 값은 행과 열의 인덱스 곱으로 초기화해 출력하는 프로그램을 작성하십시오.
'''

numbers = input()

numbers_split = numbers.split(',')
row = int(numbers_split[0].strip())
column = int(numbers_split[1].strip())

lists = []

for row_idx in range(0,row) :
    row_list = []
    for column_idx in range(0,column):
        row_list.append(row_idx*column_idx)
    lists.append(row_list)

print(lists)