def solution(num):
    count = 0
    while num != 1:
        if count > 500:
            return -1
        else:
            if num % 2:
                num = num * 3 + 1
            else:
                num = num / 2
            count += 1
    return count


solution(16)  # 4
solution(626331)  # -1
