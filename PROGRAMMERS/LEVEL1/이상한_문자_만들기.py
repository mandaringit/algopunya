def solution(s):
    answer = ''

    # 단어는 하나이상의 공백문자로 구분되어 있다. => split으로 하기 어렵다
    idx = 0

    for char in s:
        if char == " ":
            idx = 0
            answer += " "
        else:
            # 인덱스 따라 변형해 추가
            if idx % 2:
                answer += char.lower()
                idx += 1
            else:
                answer += char.upper()
                idx += 1

    return answer


solution("try hello world")
