import sys

sys.stdin = open('input.txt', 'r')


def solution(user_id, banned_id):
    matches = []

    for b_id in banned_id:
        match_set = []
        for u_id in user_id:
            # 매칭 확인
            is_match = True
            if len(b_id) == len(u_id):  # 길이가 같고
                for i in range(len(b_id)):
                    if b_id[i] == '*':  # 별일땐 넘어감
                        continue
                    elif b_id[i] == u_id[i]:  # 같으면 넘어감
                        continue
                    else:
                        is_match = False
                        break

                if is_match:
                    match_set.append(u_id)
        matches.append(match_set)

    result_banned = set()
    stack = []
    for p in matches[0]:
        stack.append([[p], 1])  # 넣은것들, 카운트

    while stack:
        banned_arr, count = stack.pop()

        if count == len(matches):
            result_banned.add(tuple(sorted(banned_arr)))
        else:
            for np in matches[count]:
                if np not in banned_arr:
                    stack.append([banned_arr + [np], count + 1])
    answer = len(result_banned)
    return answer


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
