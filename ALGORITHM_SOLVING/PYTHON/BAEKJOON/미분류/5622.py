number_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()

total_time = 0
for char in word:
    for idx, alphabets in enumerate(number_list):
        if char in alphabets:
            total_time += idx+3
print(total_time)
