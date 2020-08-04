'''
다음의 결과와 같이 입력된 문자열의 문자 빈도수를 구하는 프로그램을 작성하십시오.

입력
abcdefgabc

출력
a,2
b,2
c,2
d,1
e,1
f,1
g,1
'''

input_str = input()

rate = {}

for alphabet in input_str:
    if alphabet in rate:
        rate[alphabet] +=1
    else :
        rate[alphabet] = 1

for key,value in rate.items():
    print("{},{}".format(key,value))