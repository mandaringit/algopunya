'''
다음과 같이 문장을 구성하는 단어를 역순으로 출력하는 프로그램을 작성하십시오.

입력
A better tomorrow

출력
tomorrow better A
'''


input_str = input()

words = input_str.split(" ")

reverse_word = ""

for idx,word in enumerate(reversed(words)):
    if idx == len(words)-1:
        reverse_word += "{}".format(word)
    else:
        reverse_word += "{} ".format(word)

print(reverse_word)