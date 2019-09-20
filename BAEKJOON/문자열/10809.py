S = input()
alphabets = 'abcdefghijklmnopqrstuvwxyz'

result = ''
for alphabet in alphabets:
    result += f"{S.find(alphabet)} "
print(result.rstrip())
