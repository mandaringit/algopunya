'''
다음의 결과와 같이 정수를 입력하면 약수를 리스트에 추가해 출력하는 코드를 작성하십시오
'''

input_number = int(input())

yacsu = []

for i in range(1,input_number+1):
    if input_number % i == 0:
        yacsu.append(i)

print(yacsu)