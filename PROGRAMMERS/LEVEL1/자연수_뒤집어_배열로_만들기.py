def solution(n):
    n_list = list(map(int, str(n)))
    n_list.reverse()
    return n_list


solution(12345)  # [5,4,3,2,1]
