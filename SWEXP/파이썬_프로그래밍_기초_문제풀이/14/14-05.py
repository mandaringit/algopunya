'''
사용자가 입력한 문장에서 공백을 이용해 단어들을 구분하고,

중복된 단어없이 단어를 콤마(,)로 구분해 사전순으로 출력하는 프로그램을 작성하십시오.
'''

input_str = input()

words = input_str.split(" ")
words_set = set(words)
words_list = list(words_set)
words_list.sort()

result = ""
for idx,word in enumerate(words_list):
    if idx == len(words_list)-1:
        result += "{}".format(word)
    else :
        result += "{},".format(word)
print(result)