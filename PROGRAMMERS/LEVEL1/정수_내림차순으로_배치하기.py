def solution(n):
    n_list = list(str(n))
    n_list.sort()
    n_list.reverse()

    return int("".join(n_list))


solution(118372)  # 873211
