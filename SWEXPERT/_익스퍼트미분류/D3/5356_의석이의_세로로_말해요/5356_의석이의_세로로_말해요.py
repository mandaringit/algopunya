def paddingRight(words, length):
    for idx, word in enumerate(words):
        if len(word) != length:
            words[idx] = word + "-" * (length - len(word))
    return words


T = int(input())

for t in range(1, T + 1):
    words = []

    max_word_length = 0

    for _ in range(5):
        word = input()
        words.append(word)
        if len(word) > max_word_length:
            max_word_length = len(word)

    words = paddingRight(words, max_word_length)

    answer = ""

    for word in list(zip(*words)):
        answer += "".join(word)

    print(f"#{t} {answer.replace('-', '')}")
