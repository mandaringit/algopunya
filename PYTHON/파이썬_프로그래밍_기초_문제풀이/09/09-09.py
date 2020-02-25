'''
다음의 결과와 같이 'abcdef' 문자열의 각각의 문자를 키로 하고 0~5 사이의 정수를

값으로 하는 딕셔너리 객체를 생성하고, 이 딕셔너리 객체의 키와 값 정보를 출력하는

프로그램을 작성하십시오.

[출력]
a: 0
b: 1
c: 2
d: 3
e: 4
f: 5
'''

str = 'abcdef'
make_dic = {}
num = 0
for alphabet in str:
    make_dic[alphabet]=num
    num += 1

for key,value in make_dic.items():
    print("{}: {}".format(key,value))