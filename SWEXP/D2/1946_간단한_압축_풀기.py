T = int(input())

for tc in range(1, T + 1):

    zip_count = int(input())
    total_word = ""
    result_word = f"#{tc}\n"

    for word_count in range(zip_count):
        zip_word = input().split()
        total_word += zip_word[0] * int(zip_word[1])

    for idx, char in enumerate(total_word):
        result_word += char
        if idx % 10 == 9:
            result_word += "\n"

    print(result_word)

"""
#테스트 끄적
total_word = "A"*10 + "B"*8 + "C"*8 +"D"*10 
print(total_word)

result_word = ""
line = 0
for idx,char in enumerate(total_word):
    result_word += char
    if idx == 9 + line * 10:
        result_word += "\n"
        line+=1
    
print(result_word)
"""
