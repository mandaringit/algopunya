def solution(arr1, arr2):
    answer = []
    zip_arr = list(zip(arr1, arr2))

    for arr in zip_arr:
        arr1 = arr[0]
        arr2 = arr[1]
        result = []

        for idx, element in enumerate(arr1):
            sum_element = element + arr2[idx]
            result.append(sum_element)

        answer.append(result)

    return answer
