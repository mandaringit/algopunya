import sys

sys.stdin = open('input.txt', 'r')


for tc in range(1, 11):
    N, password = input().split()

    stack = list()

    for num in password:
        if stack:
            if stack[-1] == num:
                stack.pop(-1)
            else:
                stack.append(num)
        else:
            stack.append(num)

    print(f"#{tc} {''.join(stack)}")


# 클래스로 해보기
class PasswordStack:

    def __init__(self):
        self.data = []
        self.top = -1

    def weired_push(self, element):
        if self.top == -1:
            self.data.append(element)
            self.top += 1
        else:
            if element == self.data[self.top]:
                self.data.pop(-1)
                self.top -= 1
            else:
                self.data.append(element)
                self.top += 1


# for tc in range(1, 11):
#
#     N, password = input().split()
#     stack = PasswordStack()
#
#     for num in password:
#         stack.weired_push(num)
#
#     print(f"#{tc} {''.join(stack.data)}")
