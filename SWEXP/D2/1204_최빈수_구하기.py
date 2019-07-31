"""
#1
# 실행시간 1286ms
cases = int(input())

for case_count in range(cases):
    case_number = int(input())
    scores = list(map(int,input().split()))

    biggest_often = 0
    its_number = 0

    for score in scores:
        if scores.count(score) > biggest_often:
            biggest_often = scores.count(score)
            its_number = score
        elif scores.count(score) == biggest_often:
            if its_number < score:
                its_number = score 

    print(f"#{case_number} {its_number}")
"""
# 2
# 실행시간 176ms
cases = int(input())

for case_count in range(cases):
    case_number = int(input())
    scores = list(map(int, input().split()))

    scores_dict = {}

    biggest_often = 0
    its_number = 0

    for score in scores:
        scores_dict[score] = scores_dict[score] + \
            1 if score in scores_dict else 1

    for score, count in scores_dict.items():
        if count > biggest_often:
            biggest_often = count
            its_number = score
        elif count == biggest_often:
            if its_number < score:
                its_number = score

    print(f"#{case_number} {its_number}")
