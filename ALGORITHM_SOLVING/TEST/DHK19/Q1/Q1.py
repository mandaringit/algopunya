# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, B, C, D):
    # write your code in Python 3.6
    numbers = list(map(str, [A, B, C, D]))
    number_set = set()
    for i in range(4):
        for j in range(4):
            if j != i:
                for k in range(4):
                    if k != i and k != j:
                        for m in range(4):
                            if m != i and m != j and m != k:
                                # print(i,j,k,m)
                                hour = int(numbers[i] + numbers[j])
                                minute = int(numbers[k] + numbers[m])
                                if 0 <= hour < 24 and 0 <= minute < 60:
                                    number_set.add((hour, minute))

    return len(number_set)


solution(2, 3, 3, 2)
