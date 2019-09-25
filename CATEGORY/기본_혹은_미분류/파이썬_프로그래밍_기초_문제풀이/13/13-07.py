'''
다음과 같이 사용자가 입력한 문장에서 대소문를 구별해 각각의 갯수를 출력하는 프로그램을 작성하십시오.
'''

input_str = input()

text = {
    "UPPER CASE": 0,
    "LOWER CASE": 0
}

for i in input_str:
    if i.isalpha():
        if i.isupper():
            text["UPPER CASE"] += 1
        elif i.islower():
            text["LOWER CASE"] += 1

for key in text:
    print("{} {}".format(key,text[key]))