def solution(answers):

    answer = []

    students = {
        1: [1, 2, 3, 4, 5],
        2: [2, 1, 2, 3, 2, 4, 2, 5],
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }

    students_count = {1: 0, 2: 0, 3: 0}

    # 답마다 각 학생의 정답 카운트

    for idx, ans in enumerate(answers):
        for student_number, answer_list in students.items():
            ans_idx = idx % len(answer_list)

            if answer_list[ans_idx] == ans:
                students_count[student_number] += 1

    # 카운트로 정답 정렬하기

    max_count = max(students_count.values())

    for student_number, count in students_count.items():
        if count == max_count:
            answer.append(student_number)

    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))


# 좀 걸린 이유 => 2번 학생의 정답 리스트를 잘못넣었었음 ㅎㅅㅎ; 바보


# 1 최초풀이
"""
def solution(answers):
    answer = []

    student_answers = {
        1: [1, 2, 3, 4, 5],
        2: [2, 1, 2, 3, 2, 4, 2, 5],
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }

    # 맞춘 개수 초기화
    solve_count = {1: 0, 2: 0, 3: 0}

    for idx, real_ans in enumerate(answers):
        for s_number, value in student_answers.items():
            ans_idx = idx % len(value)
            if value[ans_idx] == real_ans:
                solve_count[s_number] += 1

    counts = []

    for count in solve_count.values():
        counts.append(count)

    top_score = max(counts)

    for solver_number, count in solve_count.items():
        if count == top_score:
            answer.append(solver_number)

    #오름차순 정렬
    answer.sort()

    return answer
"""
