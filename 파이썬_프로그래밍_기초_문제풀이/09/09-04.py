# ASCII 코드 값를 입력받아 문자를 확인하는 코드를 작성하십시오.

ascii_input = int(input())

def ascii_to_char(ascii_number):
    char = chr(ascii_number)
    print("ASCII {} => {}".format(ascii_number,char))

ascii_to_char(ascii_input)