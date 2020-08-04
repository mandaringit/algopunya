"""
문자열 단어 단위로 반전하기
"""


def reverser(string1, p1=0, p2=None):
    if len(string1) < 2:
        return string1

    p2 = p2 or len(string1) - 1

    while p1 < p2:
        string1[p1], string1[p2] = string1[p2], string1[p1]
        p1 += 1
        p2 -= 1


def reversing_words_sentence_logic(string1):
    # 먼저 문장 전체 반전
    reverser(string1)
    # print(string1)
    p = 0
    start = 0
    while p < len(string1):
        if string1[p] == u"\u0020":
            reverser(string1, start, p - 1)
            start = p + 1

        p += 1

    reverser(string1, start, p - 1)
    return "".join(string1)


if __name__ == "__main__":
    str1 = "파이썬 알고리즘 정말 재미있다"
    str2 = reversing_words_sentence_logic(list(str1))
    print(str2)
