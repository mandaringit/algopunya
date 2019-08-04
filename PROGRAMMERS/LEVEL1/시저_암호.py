# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식 => 시저 암호
def solution(s, n):
    answer = ''

    # 숫자로 변형
    ord_list = list(map(ord, s))

    for ord_num in ord_list:
        # 공백
        shifted_num = ord_num

        # 대문자
        if 65 <= ord_num <= 90:
            shifted_num = ord_num + n
            if shifted_num > 90:
                shifted_num -= 26  # 91이면 65가 됨.(Z -> A) 구간

        # 소문자
        elif 97 <= ord_num <= 122:
            shifted_num = ord_num + n
            if shifted_num > 122:
                shifted_num -= 26  # 123 이면 97이 됨.(z -> a) 구간

        answer += chr(shifted_num)

    return answer


print(solution("AB", 25))  # "BC"
print(solution("z", 1))  # "a"
print(solution("a B z", 25))  # "e F d"


# A ~ Z => 65 ~ 90
# a ~ z => 97 ~ 122
# print(ord("A"))
# print(ord("Z"))
# print(ord("a"))
# print(ord("z"))
