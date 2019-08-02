'''

다음의 결과와 같이 입력된 문자가 대문자일 경우 소문자로, 소문자일 경우 대문자로 변경하고,

알파벳이 아닐 경우엔 그냥 출력하는 코드를 작성하십시오.

출력 시 아스키코드를 함께 출력합니다.
'''

text = input()
isUpper = text.isupper()
isAlphabet = text.isalpha()

if not isAlphabet or len(text) > 1:
    print(text)
else :
    if isUpper:
        print("%c(ASCII: %d) => %c(ASCII: %d)"%(text,ord(text),text.lower(),ord(text.lower())))
    else:
        print("%c(ASCII: %d) => %c(ASCII: %d)" % (text, ord(text), text.upper(), ord(text.upper())))