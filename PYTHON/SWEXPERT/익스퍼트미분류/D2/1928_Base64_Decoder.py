"""
# 모듈 이용
# 치사합니다
import base64
encoded_word = "TGlmZSBpdHNlbGYgaXMgYSBxdW90YXRpb24u"

print(base64.b64decode(encoded_word).decode('utf-8'))
"""

base64_table = {}
table_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
value = 0
for key in table_list:
    base64_table[key] = value
    value += 1

T = int(input())

for tc in range(1, T + 1):
    encoded_word = input()
    decoded_word = ""

    bit6characters = []

    bit6char = ""
    char_count = 0

    for bit in encoded_word:
        bit6char += bit
        if char_count == 3:
            bit6characters.append(bit6char)
            bit6char = ""
            char_count = 0
        else:
            char_count += 1

    for bit6word in bit6characters:

        binary6bit = ""

        for char in bit6word:

            number = base64_table[char]
            binaryNbit = f"{number:b}"
            before6bitbinary = ""
            if len(binaryNbit) != 6:
                before6bitbinary = (6 - len(binaryNbit)) * "0" + binaryNbit
                binary6bit += before6bitbinary
            else:
                binary6bit += binaryNbit

        bit8_before_decode = []

        cnt = 0
        bit8binary = ""
        for char in binary6bit:
            bit8binary += char
            if cnt == 7:
                bit8_before_decode.append(bit8binary)
                bit8binary = ""
                cnt = 0
            else:
                cnt += 1

        total_word = ""

        for binary in bit8_before_decode:
            word = int(binary, 2)
            total_word += chr(word)
        decoded_word += total_word

    print(f"#{tc} {decoded_word}")

"""
# 테스트 끄적
# Base64 테이블 생성
base64_table={}
table_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
value = 0
for key in table_list:
    base64_table[key] = value
    value +=1

print(f"base64테이블 => {base64_table}\n")
# 한문장을 완벽하게 바꿔보자
encoded_word = "T25seSB0aGUganVzdCBtYW4gZW5qb3lzIHBlYWNlIG9mIG1pbmQu"
# 나중에 해독될 문장
decoded_word = ""

# 4개씩 나누고, 리스트에 저장
bit6characters = []

bit6char = ""
char_count = 0

for bit in encoded_word:
    bit6char += bit
    if char_count == 3:
        bit6characters.append(bit6char)
        bit6char =""
        char_count = 0
    else:
        char_count +=1

print(f"bit6characters => {bit6characters}\n")

# 각  6비트단어들마다 루프

for bit6word in bit6characters:
    
    # 6비트 2진수 만들어 합치기
    binary6bit = ""
    
    for char in bit6word:
        
        number = base64_table[char]
        binaryNbit = f"{number:b}"
        before6bitbinary = ""
        if len(binaryNbit) != 6:
            before6bitbinary = (6-len(binaryNbit))*"0" + binaryNbit
            binary6bit += before6bitbinary
        else:
            binary6bit += binaryNbit
    print(f"{bit6word} => {binary6bit}")
    
    # 합친 2진수 8개씩 나누기
    bit8_before_decode = []

    cnt = 0
    bit8binary = ""
    for char in binary6bit:
        bit8binary +=char
        if cnt == 7:
            bit8_before_decode.append(bit8binary)
            bit8binary =""
            cnt = 0
        else:
            cnt +=1
    print(f"=> {bit8_before_decode}")
    
    # 8개씩 나눈 이진수 바꾸기
    total_word = ""
    for binary in bit8_before_decode:
        word = int(binary,2)
        total_word += chr(word)
    decoded_word += total_word
    print(f"=> {total_word} \n")
print(f"해독된 문장 => {decoded_word}")
"""
