# 딕셔너리로 만들고, 서로 비교하는 방법
def solution(participant, completion):
    answer = ''

    participant_dict = {}
    for people in participant:
        if people in participant_dict:
            participant_dict[people] += 1
        else:
            participant_dict[people] = 1

    completion_dict = {}
    for people in completion:
        if people in completion_dict:
            completion_dict[people] += 1
        else:
            completion_dict[people] = 1
    # 동명이인이 있다..

    for people_name, count in participant_dict.items():
        if people_name in completion_dict:
            if count == completion_dict[people_name]:
                continue
            else:
                answer = people_name
        else:
            answer = people_name

    return answer
