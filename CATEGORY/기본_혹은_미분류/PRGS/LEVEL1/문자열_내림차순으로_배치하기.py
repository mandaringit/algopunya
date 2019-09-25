def solution(s):
    slist = sorted(list(s))
    slist.reverse()
    answer = "".join(slist)
    return answer


solution("Zbcdefg")
