import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    number_of_student, target_number = map(int, input().split())

    ratio = number_of_student // 10

    scores = []
    target_score = 0
    for k in range(1, number_of_student + 1):
        middle, final, homework = map(int, input().split())

        score = middle * 0.35 + final * 0.45 + homework * 0.2
        scores.append(score)

        if k == target_number:
            target_score = score

    scores.sort()
    scores.reverse()

    print(f"#{tc} {grades[scores.index(target_score)//ratio]}")
