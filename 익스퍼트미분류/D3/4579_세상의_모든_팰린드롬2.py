def is_palindrome(word):
    return word == word[::-1]


T = int(input())

for tc in range(1, T + 1):

    word = input()

    result = 'Not exist'

    if "*" in word:
        # "*"이 중간에 하나만 들어간다는 소리는 아무도 안했죠?
        split_words = word.split("*")
        # "*"로 나눠진게 얼마나 많던지 우린 앞과 뒤만 보면 된다.
        front, end = split_words[0], split_words[-1]

        min_len = min((len(front), len(end)))

        if min_len == 0:
            result = 'Exist'
        else:
            new_word = front[:min_len] + end[-min_len:]
            if is_palindrome(new_word):
                result = 'Exist'

    else:
        if is_palindrome(word):
            result = 'Exist'

    print(f"#{tc} {result}")
