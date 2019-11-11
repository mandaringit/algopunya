""" #1
alphabets = input()

for alphabet in alphabets:
    print(ord(alphabet)-64,end=" ")
"""

# 2
# 샘플을 줘서 만들고 해야지 바보야
alphabet_sample = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_dict = {alphabet: idx+1 for idx, alphabet in enumerate(alphabet_sample)}

alphabets = input()

for idx, alphabet in enumerate(alphabets):
    print(alpha_dict[alphabet], end=" ")
