T = int(input())

for tc in range(1, T + 1):
    word = input()

    new_word = ''
    for char in word:
        if char not in 'aeiou':
            new_word += char

    print(f"#{tc} {new_word}")
