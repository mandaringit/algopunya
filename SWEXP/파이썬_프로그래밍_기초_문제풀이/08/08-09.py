'''
인자로 전달된 두 개의 문자열 중 길이가 더 긴 문자열을 출력하는 함수를 정의하고


결과를 출력하는 프로그램을 작성하십시오.
'''

def calc_str_length():
    str = input()

    strings = str.split(",")

    longestString = ''

    for string in strings:
        strippedStr = string.strip()
        if len(strippedStr) > len(longestString):
            longestString = strippedStr

    return longestString

print(calc_str_length())
