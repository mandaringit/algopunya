# 테스트 끄적

grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

test_case = int(input())

for case_number in range(test_case):
    student_count, student_number = (int(num) for num in input().split())

    score_list = []

    ratio = round(student_count/10)

    for i in range(student_count):
        # 점수 인풋으로 받아서 나누기 , 중간,기말,과제 순
        score = [int(num) for num in input().split()]
        total_score = score[0] * 0.35 + score[1] * 0.45 + score[2] * 0.2
        score_list.append(total_score)

    print(score_list)
    target_score = score_list[student_number-1]
    score_list.sort()
    score_list.reverse()
    rank = score_list.index(target_score) // ratio
    print(f"#{case_number + 1} {grade[rank]}")

"""
grade = ["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"]
student_count,student_number = (10,2)

case = [
    [87, 59 ,88],
[99, 94 ,78],
[94, 86 ,86],
[99 ,100 ,99],
[69, 76 ,70],
[76, 89 ,96],
[98, 95 ,96],
[74, 69 ,60],
[98, 84, 67],
[85, 84 ,91]
]
# 점수 리스트 구하기

score_list = []

# 학점비율
ratio = round(student_count/10)

for score in case:
#     score = list(map(int,input().split()))  # 점수 인풋으로 받아서 나누기 , 중간,기말,과제 순
    total_score = score[0] * 0.35 + score[1] * 0.45 + score[2] * 0.2
    score_list.append(total_score)

target_score = score_list[student_number-1]

score_list.sort()
score_list.reverse()
rank = score_list.index(target_score) // ratio
print(rank)
print(grade[rank])
"""
