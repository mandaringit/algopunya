def solution(s):
    answer = ''

    half = len(s) // 2

    # 홀수
    if len(s) % 2:
        answer = s[half]
    # 짝수
    else:
        answer = s[half-1: half+1]
    return answer
