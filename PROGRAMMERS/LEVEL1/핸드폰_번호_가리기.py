def solution(phone_number):
    answer = "*"*(len(phone_number)-4) + phone_number[-4:]
    return answer


solution("01033334444")  # '*******4444'
solution("027778888")  # '*****8888'
