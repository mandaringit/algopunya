# 시간초과

import sys

sys.stdin = open('input.txt', 'r')


def NGE(top, stack):
    result = []
    popped_list = []
    for i in range(top, 0, -1):

        if i == top:
            result.append(-1)
        else:
            popped = stack.pop()
            popped_list.append(popped)

            if popped > stack[i - 1]:
                result.append(popped)
            else:
                isExist = False
                for j in range(len(popped_list) - 1, -1, -1):
                    if popped_list[j] > stack[i - 1]:
                        result.append(popped_list[j])
                        isExist = True
                        break

                if not isExist:
                    result.append(-1)

    return result[::-1]


top = int(input())
stack = list(map(int, input().split()))

print(" ".join(map(str, NGE(top, stack))))
