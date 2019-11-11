import sys

sys.stdin = open('input.txt', 'r')


def BFS(number):
    global C
    global maxV
    numbers = list(number)

    q = [(numbers, 0)]
    even_visited = []
    odd_visited = []

    while q:
        digits, count = q.pop(0)

        if count == C:
            num = int(''.join(digits))
            if num > maxV:
                maxV = num
        else:
            for i in range(len(numbers)):
                for j in range(i + 1, len(numbers)):
                    cp_nums = digits[:]
                    cp_nums[i], cp_nums[j] = cp_nums[j], cp_nums[i]
                    join_num = ''.join(cp_nums)

                    go = True

                    if (count + 1) % 2 == 0:
                        if int(join_num) in odd_visited:
                            go = False
                        else:
                            odd_visited.append(int(join_num))
                    else:
                        if join_num in even_visited:
                            go = False
                        else:
                            even_visited.append(int(join_num))

                    if count + 1 == C:
                        num = int(''.join(cp_nums))
                        if num > maxV:
                            maxV = num
                    if go:
                        q.append((cp_nums, count + 1))
    if maxV == 0:
        if C % 2 == 0:
            maxV = max(odd_visited)
        else:
            maxV = max(even_visited)


T = int(input())

for tc in range(1, T + 1):
    number, C = input().split()
    C = int(C)
    maxV = 0

    BFS(number)

    print("#{} {}".format(tc, maxV))
