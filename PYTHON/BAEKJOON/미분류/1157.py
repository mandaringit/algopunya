word = input()
upper_word = word.upper()

word_dict = {}

for char in upper_word:
    if char in word_dict:
        word_dict[char] += 1
    else:
        word_dict[char] = 1


most_char = '?'
most_often = 0

for key, value in word_dict.items():
    if value > most_often:
        most_often = value
        most_char = key
    elif value == most_often:
        most_char = '?'

print(most_char)
