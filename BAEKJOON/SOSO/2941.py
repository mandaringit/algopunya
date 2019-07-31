# 크로아티아
# 간단하게 갯수만 세보기
chro_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()

for chro in chro_list:
    if chro in word:
        word = word.replace(f"{chro}", "0")
print(len(word))

"""
# 크로아티아 변경하기
chro_dict = {"c=":"č","c-":"ć","dz=":"dž","d-":"đ","lj":"lj","nj":"nj","s=":"š","z=":"ž"}

word = "ljes=njak"

for alpha, chro in chro_dict.items():
    if alpha in word:
        word = word.replace(f"{alpha}", chro)
print(word)
"""
