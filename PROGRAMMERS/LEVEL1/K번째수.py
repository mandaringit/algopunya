def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command

        slice_list = sorted(array[i-1:j])
        pick_element = slice_list[k-1]
        answer.append(pick_element)

    return answer


solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
