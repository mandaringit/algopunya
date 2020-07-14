def solution(s):
    # 길이 N개 단위로 자를때. 문자열 길이?

    word_length = len(s)

    def cutting(n):
        zip_strings = []
        start_idx = 0
        for last_idx in range(n, word_length + 1, n):

            # 자른 단어
            split_word = s[start_idx:last_idx]

            # 일단 첫 단어는 그냥 넣습니다.
            if start_idx == 0:
                zip_strings.append([split_word, 1])  # 단어, 카운팅
            # 그 이후에는
            else:
                # 묶은 단어중 지금 자른 단어가 이전 자른 단어랑 같을때
                recent_word = zip_strings[-1]
                if split_word == recent_word[0]:
                    zip_strings[-1][1] += 1
                # 안같으면 그냥 넣는다.
                else:
                    zip_strings.append([split_word, 1])

            # 그다음 단어로 가기 위해 인덱스 이동.
            start_idx = last_idx

        # 만약 나머지가 있는경우
        rest = word_length % n

        if rest:
            zip_strings.append([s[-rest:], 1])

        string = ''
        for word, count in zip_strings:
            if count > 1:
                string += f'{count}{word}'
            else:
                string += word

        return string

    # 압축 단어 길이 비교
    minV = word_length
    for i in range(1, word_length + 1):
        length = len(cutting(i))
        if length < minV:
            minV = length

    return minV


import unittest


class MyTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(solution("aabbaccc"), 7)

    def test_case2(self):
        self.assertEqual(solution("ababcdcdababcdcd"), 9)

    def test_case3(self):
        self.assertEqual(solution("abcabcdede"), 8)

    def test_case4(self):
        self.assertEqual(solution("abcabcabcabcdededededede"), 14)

    def test_case5(self):
        self.assertEqual(solution("xababcdcdababcdcd"), 17)
