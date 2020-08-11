import sys

sys.stdin = open('input.txt', 'r')

number = input()


def solution(number):
    number_list = sorted(list(map(int, list(number))), reverse=True)
    if number_list[-1] == 0 and sum(number_list) % 3 == 0:
        return ''.join(map(str, number_list))
    else:
        return -1


print(solution(number))
