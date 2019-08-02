'''
다음의 결과와 같이 이름과 나이를 입력 받아

올해를 기준으로 100세가 되는 해를 표시하는 코드를 작성하십시오.
'''

name_input = input()
age_input = int(input())

def when_be_100(name,age):
    this_year = 2018
    last_year = this_year + 100 - age
    print("%s(은)는 %d년에 100세가 될 것입니다." % (name,last_year))

when_be_100(name_input,age_input)