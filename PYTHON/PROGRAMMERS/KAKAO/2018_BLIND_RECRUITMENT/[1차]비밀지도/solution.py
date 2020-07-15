def solution(n, arr1, arr2):  # 지도 한변 크기 n, 2개의 "정수"배열 arr1, arr2

    def get_bin_map(arr):
        bin_map = []
        for value in arr:
            bin_value = format(value, 'b')
            padded_value = bin_value.zfill(n)
            bin_map.append(padded_value)
        return bin_map

    map1 = get_bin_map(arr1)
    map2 = get_bin_map(arr2)

    original_map = []
    for i in range(n):
        line = ''
        for j in range(n):
            map1_value = map1[i][j]
            map2_value = map2[i][j]

            if map1_value == '0' and map2_value == '0':
                line += ' '
            else:
                line += '#'

        original_map.append(line)
    return original_map


solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
