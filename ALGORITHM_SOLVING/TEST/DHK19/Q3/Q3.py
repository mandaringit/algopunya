# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    existed_a = S.count('a')
    result = ''
    if 'aaa' in S:
        return -1
    else:
        chars = list(S)
        for idx, char in enumerate(chars):
            if char == 'a':
                if len(result) > 0 and result[-1] == 'a':
                    pass
                else:
                    result += 'a' + char
            else:
                result += 'aa' + char

            if idx == len(S) - 1:
                result += 'aa'
    result = result.replace('aaaa', 'aa')
    result = result.replace('aaa', 'aa')
    count_a = result.count('a')
    return count_a - existed_a


print(solution('aabab'))
solution('dog')
solution('aa')
solution('baaa')
