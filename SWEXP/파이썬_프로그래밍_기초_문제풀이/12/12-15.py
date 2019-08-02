'''
단어를 콤마(,)로 구분해 입력하면 그 단어들을 사전순으로 정렬해 출력하는 프로그램을 작성하시시오.
'''

input_words = input()

split_words_list = input_words.split(',')

dic_word = []

for word in split_words_list:
    dic_word.append(word.strip())

dic_word.sort()

result = ""
for idx,word in enumerate(dic_word):
    if idx == len(dic_word)-1:
        result += "{}".format(word)
    else :
        result+= "{}, ".format(word)

print(result)