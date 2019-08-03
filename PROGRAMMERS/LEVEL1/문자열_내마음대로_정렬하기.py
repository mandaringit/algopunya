def solution(strings, n):
    answer = []

    pick_char_list = []
    string_dict = {}

    for string in strings:
        pick_char = string[n]  # 선택된 알파벳
        pick_char_list.append(pick_char)

        # 딕셔너리로 만드는데, 중복을 위해 리스트로 만들기.
        if pick_char in string_dict:
            string_dict[pick_char].append(string)
        else:
            string_dict[pick_char] = [string]

    # pick_char_list 정렬해주기
    pick_char_list.sort()

    # string_dict를 돌면서 미리 사전순 정렬해주기
    for char in string_dict:
        string_dict[char].sort()

    string_dict_idx = 0
    for idx, char in enumerate(pick_char_list):
        # 첫번째는 무조건 넣어주고
        if idx == 0:
            answer.append(string_dict[char][string_dict_idx])
        # 두번째부터
        else:
            # 이전 알파벳과 중복이라면
            if char == pick_char_list[idx-1]:
                string_dict_idx += 1
                answer.append(string_dict[char][string_dict_idx])
            # 아니라면
            else:
                string_dict_idx = 0
                answer.append(string_dict[char][string_dict_idx])

    return answer


solution(["sun", "bed", "car"], 1)  # ["car","bed","sun"]
solution(["abce", "abcd", "cdx"], 2)  # ["abcd", "abce", "cdx"]
