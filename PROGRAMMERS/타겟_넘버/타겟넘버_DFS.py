numbers = [1, 1, 1, 1, 1]


def f(numbers, i, total, target, path):
    global count
    if i == len(numbers) - 1:
        if total == target:
            count += 1
            print(path)
            return
        else:
            return
    else:
        f(numbers, i + 1, total + numbers[i + 1], target, path + [numbers[i + 1]])
        f(numbers, i + 1, total - numbers[i + 1], target, path + [-numbers[i + 1]])


count = 0


def solution(numbers, target):
    global count
    f(numbers, 0, numbers[0], target, [numbers[0]])
    f(numbers, 0, -numbers[0], target, [-numbers[0]])

    return count


print(solution(numbers, 3))
