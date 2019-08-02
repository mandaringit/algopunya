'''
다음과 같이 사용자가 입력한 문장에서 숫자와 문자를 구별해 각각의 개수를 출력하는 프로그램을 작성하십시오.
'''

input_str = input()

separate = {
    "LETTERS":0,
    "DIGITS":0
}

for i in input_str:
    if i.isdigit():
        separate["DIGITS"] +=1
    elif i.isalpha():
        separate["LETTERS"] +=1


for key in separate:
    print("{} {}".format(key,separate[key]))
